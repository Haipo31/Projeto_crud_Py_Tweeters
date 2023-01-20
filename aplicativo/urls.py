from django.urls import path
from . import views 

urlpatterns = [

    path('', views.index, name='index'),
    path('', views.twitter, name= 'twitter'),
    path('', views.usuario, name= 'usuario')

]