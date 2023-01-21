from django.db import models
from datetime import datetime

class Usuarios(models.Model):
    nome_usuario = models.CharField(max_length= 150)
    email_usuario = models.CharField(max_length= 150)
    senha_usuario = models.CharField(max_length= 30)
    descricao_twitter = models.CharField(max_length = 200)
    date_aluno = models.DateTimeField(default=datetime.now, blank=True)


