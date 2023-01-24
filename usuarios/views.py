from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import Usuarios

def cadastro(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('login')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

def autenticar(request):
    if request.method == "POST":
        email_usuario = request.POST["nome_usuario"]
        senha_usuario = request.POST["senha_usuario"]
        usuario = authenticate(request, email_usuario=email_usuario, senha_usuario=senha_usuario)
        if usuario is not None:
            login(request, usuario)
            return render(request, 'sobre.html')
        else:
            form_autenticar = AuthenticationForm()
    else:
        form_autenticar = AuthenticationForm()
    return render(request, 'twitter.html', {'form_autenticar': form_autenticar})

def login(request):
    return render(request, 'login.html')


def sobre(request):
    return render(request, 'sobre.html')

def twitter(request):
    return render(request, 'twitter.html')

def usuario(request):
    return render(request, 'usuario.html')










