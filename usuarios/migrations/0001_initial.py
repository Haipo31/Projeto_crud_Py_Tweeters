# Generated by Django 4.1.5 on 2023-01-21 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_usuario', models.CharField(max_length=150)),
                ('email_usuario', models.CharField(max_length=150)),
                ('senha_usuario', models.CharField(max_length=30)),
                ('descricao_twitter', models.CharField(max_length=200)),
                ('date_aluno', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
