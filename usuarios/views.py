from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuarios
from django.contrib.auth.models import User, auth
from django.contrib import messages

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

def cadastro(request):
    return render(request, 'cadastro.html')


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Usuarios.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')




