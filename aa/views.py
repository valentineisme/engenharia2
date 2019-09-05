from django.shortcuts import render
from .models import usuario
from .forms import UsuarioForm

def index(request):
    if request.POST:
        form = UsuarioForm(request.POST)
    else:
        form = UsuarioForm()
    return render(request, 'index.html', {'form':form})

def cadastro_usuario(request):

    if request.method == "POST":
        u = usuario()
        current_user = usuario.objects.get(cpf=request.POST.get('cpf'))
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
