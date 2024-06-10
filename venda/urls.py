from django.urls import path, include
from . import views

urlpatterns = [
    path('cad-vendas/', views.cad_venda, name='cad_vendas'),
    path('vendas/', views.vendas_list, name='vendas_list'),
    path('salvar_item/', views.salvar, name='salvar')
]
