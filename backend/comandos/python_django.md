# Comandos usados da tecnologia principal no projeto

- Python
- Django (rest framework)

## Pytho


- Criação do ambiente virtual.
    ~~~bash
    python3 -m venv venv
    ~~~
- Ativação do ambiente virtual.
    ~~~bash
    . venv/bin/activate
    ~~~
- Atualização do pip
    ~~~bash
    python3.exe -m pip install --upgrade pip
    ~~~
- Instalação do cors. Um aplicativo Django que adiciona cabeçalhos Cross-Origin Resource Sharing (CORS) às respostas
    ~~~bash
    pip install django-cors-headers
    ~~~


## Django

- Instalação do django e suas dependencias.
    ~~~bash
        pip install django
    ~~~

- Criação do core do django.
    ~~~bash
        django-admin startproject core . 
    ~~~
- Criação de um super usuario.
    ~~~bash    
        python manage.py createsuperuser
    ~~~
- Detecção de alterações nos models de dados e gera arquivos de migração que, posteriormente, seram aplicados ao banco de dados.
    ~~~bash    
        python manage.py makemigrations 
    ~~~
- Aplica as alterações feitas nos models de dados e atualiza os.
    ~~~bash    
        python manage.py migrate
    ~~~
- Rodar o servidor 
    ~~~bash    
        python manage.py runserver
    ~~~
- Instalação do JWT
    ~~~bash    
        pip install djangorestframework-simplejwt
    ~~~


## Django Rest Framework

- Instalação do django rest framework
    ~~~bash    
        pip install djangorestframework
    ~~~


## Comandos rapidos

- Atualização dos models

    ~~~bash    
        python manage.py makemigrations 
        python manage.py migrate
    ~~~