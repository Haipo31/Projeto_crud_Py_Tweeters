from django.shortcuts import render, get_object_or_404
from .models import Usuarios


def login(request):
    usuarios = Usuarios.objects.all()

    dados = {
        'usuarios': usuarios
    }

    return render(request, 'login.html', dados)

def sobre(request):
    return render(request, 'sobre.html')

def twitter(request):
    return render(request, 'twitter.html')

def usuario(request):
    return render(request, 'usuario.html')









