#!/usr/bin/env python3

import django

# iniciar um projeto no Django
django-admin.py startproject [NOME DO PROJETO] 

# rodar um servidor de desenvolvimento local
# caminho@terminal:~/pasta_projeto/projeto_djando/$
python manage.py runserver

# criar as tabelas do banco de dados
python manage.py makemigrations e 

# enviar as as tabelas para o banco de dados
python manage.py migrate
#XXX o comando syncdb não existe mais.

# criar aplicações no django
python manage.py startapp core
# core é o nome da app, contem coisa úteis para ser usado 
# nessa e em outras app's.

 


