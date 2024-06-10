from django.urls import path, include
from . import views

urlpatterns = [
    # url: .../cadastro
    path('cadastro/', views.cadastro, name='cadastro'),
    # url: .../login
    path('login/', views.login, name='login'),
    # url: .../home
    # path('', include('home.urls'), name='home:init'),
    path('home/', views.home, name='home'),
    path('home/login/', views.login),
    path('', views.login)
]
