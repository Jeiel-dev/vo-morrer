from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required
def cad_cliente(request):
    return redirect('cadastro_cli')

