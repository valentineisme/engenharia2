from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login as authlogin
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import usuario
from .forms import UsuarioForm

def index(request):
    if request.POST:
        form = UsuarioForm(request.POST)
    else:
        form = UsuarioForm()
    if request.user.id:
        current_user = usuario.objects.get(email=request.user)
        form = UsuarioForm()
        return render(request, 'index_logado.html', {'usuario': current_user, 'form': form})
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
def sair(request):
    logout(request)
    return index(request)