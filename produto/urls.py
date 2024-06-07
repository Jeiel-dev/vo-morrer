from . import views
from django.urls import path, include

urlpatterns = [
    path('produtos/', views.produtos_list, name='pruduto_list'),
    path('cadastro_produto/', views.cadastro_produto, name='cad_produtos'),
    path('salvar_produto/', views.salvar_p, name='salvar_prod'),
    path('editar_produto/<str:cod_barra>', views.editar_p, name='editar_prod'),
    path('deletar_produto/<str:cod_barra>', views.deletar_p, name='deletar_prod'),
    path('update_produto/<str:cod_barra>', views.update, name='update_produto'),
]
