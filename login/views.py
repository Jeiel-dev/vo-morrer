from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# funçao cadastro


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/cadastro.html')
    else:
        # passa as informaçoes do form. cadastro para as variaveis
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    # verifica se o usuario ja esiste no banco
    user = User.objects.filter(username=username).first()
    # se sim, retorna 'ja cadastrado'
    if user:
        return HttpResponse('ja cadastrado')
    # se nao, cria o usuario na class: User, e passa os dados para funçao user
    user = User.objects.create_user(
        username=username, email=email, password=senha)
    # salva o usuario no banco
    user.save

    return HttpResponse('cadastrado')

# funçao login


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        # passa as informaçoes do form. login para as variaveis
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        # verifica se o username e a senha consta no banco de dados
        user = authenticate(username=username, password=senha)

        if user:
            # autentica o usuario
            login_django(request, user)
            return HttpResponse(home(request))
        else:
            return HttpResponse('usuario invalido')

# verifica se o usuario esta autenticado
# se sim, manda pra pagina Home, se nao, manda para a pagina de login


@login_required(login_url='login/')
def home(request):
    return render(request, 'home/home.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')