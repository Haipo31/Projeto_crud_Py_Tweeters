from django.shortcuts import render, get_object_or_404
from .models import Usuarios


def index(request):
    usuarios = Usuarios.objects.all()

    dados = {
        'usuarios': usuarios
    }

    return render(request, 'index.html', dados)







