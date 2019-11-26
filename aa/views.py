from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login as authlogin
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import usuario, veiculos, modelo_carro, marca_carro, leilao
from .forms import UsuarioForm, VeiculoForm
from datetime import datetime

def index(request):
    if request.POST:
        form = UsuarioForm(request.POST)
    else:
        form = UsuarioForm()
    if request.user.id:
        current_user = usuario.objects.get(email=request.user)
        form = UsuarioForm()
        form_veic = VeiculoForm()
        modelo_veic = modelo_carro.objects.all()
        marca_veic = marca_carro.objects.all()
        return render(request, 'index_logado.html', {'modelos': modelo_veic, 'marcas': marca_veic,'usuario': current_user, 'form': form, 'form_veic': form_veic})
    return render(request, 'index.html', {'form': form})

def cadastro_usuario(request):

    if request.method == "POST":
        u = usuario()
        try:
            current_user = usuario.objects.get(cpf=request.POST.get('cpf'))
        except:
            current_user = ""
        if current_user == "":
            u.nome = request.POST.get('nome')
            u.cpf = request.POST.get('cpf')
            u.data_nascimento = request.POST.get('data_nascimento')
            u.telefone = request.POST.get('telefone')
            u.email = request.POST.get('email')
            u.senha = request.POST.get('senha')
            u.save()
            return index(request)
        else:
            form = UsuarioForm(request.POST)
            return render(request, 'cadastros/cad_user_error.html', {'form': form, "usuario": current_user})


def validacao(request):
    if request.user.id:
        return index(request)

    if request.POST:
        emailUser = request.POST.get('email')
        senhaUser = request.POST.get('senha')

        u = authenticate(username=emailUser, password=senhaUser)
        if u is not None:
            if u.is_active:
                authlogin(request, u)

                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return index(request)
    return login_error(request)

def login_error(request):
    if request.POST:
        form = UsuarioForm()
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    mensagem_error = 'e-mail ou senha invalidos'
    return render(request, 'index.html', {'form': form, 'mensagem':mensagem_error, 'email':email, 'senha': senha})


@login_required
def usuario_editar(request):
    if request.GET['us']:
        user_id = request.GET['us']
        current_user = usuario.objects.filter(id=user_id)
        json = serializers.serialize("json", current_user)
        return HttpResponse(json)

@login_required
def usuario_editar_final(request):
    if request.POST['id_usuario']:
        user_id = request.POST['id_usuario']
        current_user = usuario.objects.get(id=user_id)
        if current_user != "":
            current_user.nome = request.POST.get('nome')
            current_user.telefone = request.POST.get('telefone')
            current_user.data_nascimento = request.POST.get('data_nascimento')
            current_user.save()
            u = authenticate(username=current_user.email, password=current_user.senha)
            if u is not None:
                if u.is_active:
                    authlogin(request, u)

                    if request.POST.get('next'):
                        return HttpResponseRedirect(request.POST.get('next'))

                    return index(request)

@login_required
def ajax_pesquisa(request):
    if 'marca' in request.GET:
        id = request.GET['marca']
        modelos = modelo_carro.objects.filter(marca=id)
        json = serializers.serialize("json", modelos)
        return HttpResponse(json)

@login_required
def cadastro_veiculo(request):
    current_user = usuario.objects.get(email=request.user)
    if request.POST:
        v = veiculos()
        try:
            current_veiculo = veiculos.objects.get(placa=request.POST.get('placa'))
        except:
            current_veiculo = ""

        if current_veiculo == "":
            current_modelo = modelo_carro.objects.get(id = request.POST.get('modelo'))
            v.modelo = current_modelo
            v.ano_veiculo = request.POST.get('ano_veiculo')
            v.cor = request.POST.get('cor')
            v.placa = request.POST.get('placa')
            v.combustivel = request.POST.get('combustivel')
            v.valor = request.POST.get('valor')
            v.ipva = request.POST.get('ipva')
            v.documentacao = request.POST.get('documentacao')
            v.img = request.POST.get('img')
            v.observacao = request.POST.get('observacao')
            v.usuario_id = current_user
            v.save()
            return index(request)

@login_required
def leiloar_veiculo(request):
    modelo_veic = modelo_carro.objects.all()
    marca_veic = marca_carro.objects.all()
    current_user = usuario.objects.get(email=request.user)
    lista_veiculos = []
    list_veiculos = veiculos.objects.filter(usuario_id = current_user)
    for lv in list_veiculos:
        dict_veiculos = {}
        try:
            test_leilao = leilao.objects.get(veiculo_id=lv.id)
            dict_veiculos['id'] = test_leilao.veiculo_id.id
            dict_veiculos['modelo'] = test_leilao.veiculo_id.modelo
            dict_veiculos['usuario_id'] = test_leilao.veiculo_id.usuario_id
            dict_veiculos['ano_veiculo'] = test_leilao.veiculo_id.ano_veiculo
            dict_veiculos['cor'] = test_leilao.veiculo_id.cor
            dict_veiculos['combustivel'] = test_leilao.veiculo_id.combustivel
            dict_veiculos['placa'] = test_leilao.veiculo_id.placa
            dict_veiculos['valor'] = test_leilao.veiculo_id.valor
            dict_veiculos['documentacao'] = test_leilao.veiculo_id.documentacao
            dict_veiculos['ipva'] = test_leilao.veiculo_id.ipva
            dict_veiculos['img'] = test_leilao.veiculo_id.img
            dict_veiculos['observacao'] = test_leilao.veiculo_id.observacao
            dict_veiculos['status'] = test_leilao.status
            lista_veiculos.append(dict_veiculos)
        except:
            dict_veiculos['id'] = lv.id
            dict_veiculos['modelo'] = lv.modelo
            dict_veiculos['usuario_id'] = lv.usuario_id
            dict_veiculos['ano_veiculo'] = lv.ano_veiculo
            dict_veiculos['cor'] = lv.cor
            dict_veiculos['combustivel'] = lv.combustivel
            dict_veiculos['placa'] = lv.placa
            dict_veiculos['valor'] = lv.valor
            dict_veiculos['documentacao'] = lv.documentacao
            dict_veiculos['ipva'] = lv.ipva
            dict_veiculos['img'] = lv.img
            dict_veiculos['observacao'] = lv.observacao
            lista_veiculos.append(dict_veiculos)
    
    form_veic = VeiculoForm()
    paginator = Paginator(lista_veiculos, 2)
    page = request.GET.get('page')
    try:
        dados = paginator.page(page)
    except PageNotAnInteger:
        dados = paginator.page(1)
    except EmptyPage:
        dados = paginator.page(paginator.num_pages)

    data_atual = datetime.now().strftime("%Y-%m-%d")
    data_final = str(datetime.now().year)+"-"+str(datetime.now().month + 1) + "-" + str(datetime.now().day)
    return render(request, 'veiculos/lista.html', {'modelos': modelo_veic, 'marcas': marca_veic, 'form_veic': form_veic, 'dados': dados, "data_atual": data_atual, "data_final":data_final})

@login_required
def leiloando(request):
    if request.POST:
        current_user = usuario.objects.get(email=request.user)
        current_veic = veiculos.objects.get(id=request.POST.get('id_veic'))
        data_atual = datetime.now()
        l = leilao()
        l.veiculo_id = current_veic
        l.usuario_id = current_user
        l.data_inicio = data_atual
        l.data_final = request.POST.get('data_final')
        l.valor_atual = current_veic.valor
        l.status = 'ativo'
        l.save()
        return index(request)

@login_required
def em_leilao(request):
    current_user = usuario.objects.get(email = request.user)
    current_leilao = leilao.objects.filter(usuario_id = current_user)
    leiloes = []
    for l in current_leilao:
        l_dict = {}
        try:
            user_buy = usuario.objects.get(id = int(l.usuario_id_comprador))
            l_dict['id_veiculo'] = l.veiculo_id.id
            l_dict['modelo'] = l.veiculo_id.modelo
            l_dict['usuario_id'] = l.veiculo_id.usuario_id
            l_dict['usuario_id_comprador'] = user_buy
            l_dict['ano_veiculo'] = l.veiculo_id.ano_veiculo
            l_dict['cor'] = l.veiculo_id.cor
            l_dict['combustivel'] = l.veiculo_id.combustivel
            l_dict['placa'] = l.veiculo_id.placa
            l_dict['valor'] = l.veiculo_id.valor
            l_dict['documentacao'] = l.veiculo_id.documentacao
            l_dict['ipva'] = l.veiculo_id.ipva
            l_dict['img'] = l.veiculo_id.img
            l_dict['observacao'] = l.veiculo_id.observacao
            l_dict['status'] = l.status
            l_dict['valor_inicial'] = l.valor_inicial
            l_dict['valor_atual'] = l.valor_atual
            l_dict['data_final'] = l.data_final
            l_dict['mensagem'] = "proposta ativa"
            leiloes.append(l_dict)
            
        except:
            l_dict['id_veiculo'] = l.veiculo_id.id
            l_dict['modelo'] = l.veiculo_id.modelo
            l_dict['usuario_id'] = l.veiculo_id.usuario_id
            l_dict['usuario_id_comprador'] = l.usuario_id_comprador
            l_dict['ano_veiculo'] = l.veiculo_id.ano_veiculo
            l_dict['cor'] = l.veiculo_id.cor
            l_dict['combustivel'] = l.veiculo_id.combustivel
            l_dict['placa'] = l.veiculo_id.placa
            l_dict['valor'] = l.veiculo_id.valor
            l_dict['documentacao'] = l.veiculo_id.documentacao
            l_dict['ipva'] = l.veiculo_id.ipva
            l_dict['img'] = l.veiculo_id.img
            l_dict['observacao'] = l.veiculo_id.observacao
            l_dict['status'] = l.status
            l_dict['valor_inicial'] = l.veiculo_id.valor
            l_dict['valor_atual'] = l.valor_atual
            l_dict['data_final'] = l.data_final
            l_dict['mensagem'] = "nenhuma proposta"
            leiloes.append(l_dict)

    paginator = Paginator(leiloes, 2)
    page = request.GET.get('page')
    try:
        dados = paginator.page(page)
    except PageNotAnInteger:
        dados = paginator.page(1)
    except EmptyPage:
        dados = paginator.page(paginator.num_pages)

    return render(request, 'veiculos/em_leilao.html', {'dados': dados})

@login_required
def leilao_ativo(request):
    current_user = usuario.objects.get(email = request.user)
    current_leilao = leilao.objects.filter(status = "ativo").exclude(usuario_id = current_user)


    paginator = Paginator(current_leilao, 2)
    page = request.GET.get('page')
    try:
        dados = paginator.page(page)
    except PageNotAnInteger:
        dados = paginator.page(1)
    except EmptyPage:
        dados = paginator.page(paginator.num_pages)

    return render(request, 'veiculos/leilao_ativo.html', {'dados': dados})

@login_required
def leilao_ativar(request):
    if request.POST:
        current_user = usuario.objects.get(email = request.user)
        current_leilao = leilao.objects.get(id = request.POST.get('id_leilao'))
        if request.POST.get('valor_proposto') < current_leilao.valor_atual:
            return leilao_ativo(request)
        else:
            current_leilao.valor_atual = request.POST.get('valor_proposto')
            current_leilao.usuario_id_comprador = current_user.id
            current_leilao.save()
            return lances(request)

@login_required
def lances(request):
    current_user = usuario.objects.get(email = request.user)
    current_leilao = leilao.objects.filter(usuario_id_comprador = current_user.id)


    paginator = Paginator(current_leilao, 2)
    page = request.GET.get('page')
    try:
        dados = paginator.page(page)
    except PageNotAnInteger:
        dados = paginator.page(1)
    except EmptyPage:
        dados = paginator.page(paginator.num_pages)

    return render(request, 'veiculos/lances.html', {'dados': dados})


@login_required
def sair(request):
    logout(request)
    return index(request)