from django.urls import path
from . import views 

urlpatterns = [

    path('', views.cadastro, name='cadastro'),
    path('sobre', views.sobre, name='sobre'),
    path('twitter', views.twitter, name='twitter'),
    path('usuario', views.usuario, name='usuario'),
    path('login', views.login, name='login')

    

]