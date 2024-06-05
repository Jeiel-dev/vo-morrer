from django.shortcuts import render, redirect
from django.contrib import auth


def home(request):
    return render(request, 'home.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


