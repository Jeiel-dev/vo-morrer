from django.urls import path
from . import views

urlpatterns = [
    # url: .../cadastro
    path('cadastro/', views.cadastro, name='cadastro'),
    # url: .../login
    path('login/', views.login, name='login'),
    # url: .../home
    path('home/', views.home, name='home')
]
