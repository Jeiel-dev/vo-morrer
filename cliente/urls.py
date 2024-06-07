from django.urls import path, include
from . import views
from home.views import home

urlpatterns = [
    path('cadastro_cliente/', views.cadastro, name='cadastro_cli'),
    path('salvar/', views.salvar, name='salvar_cli'),
    path('', views.home , name='home'),
    path('clientes/', views.lista_clientes , name='clientes'),
    path('editar/<str:cpf>', views.editar , name='editar'),
    path('update/<str:cpf>', views.update , name='update'),
    path('delet/<str:cpf>', views.delet , name='delet'),
    # path('clientes/<str:cpf>', views.excluir , name='excluir'),
    
]
