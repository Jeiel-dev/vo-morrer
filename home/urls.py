from django.urls import path
from . import views
from cliente import views as views_cliente
from produto import views as views_produto
from pedido import views as views_pedio

urlpatterns = [
    # url: .../cadastro
    # path(views.home, name='home'),
    # path('home-/', views.home, name='init')
    path('logout/', views.logout, name='logout'),
    path('home/cadastro_cliente/', views_cliente.cadastro, name='cad_cliente'),
    path('home/clientes/', views_cliente.lista_clientes, name='clientes'),
    path('home/cadastro_produto/', views_produto.cadastro_produto, name='cad_produto'),
    path('home/produtos_list/', views_produto.produtos_list, name='produtos'),
    # path('home/cad_vendas', views_venda.cad_vendas, name='cad_vendas')
    # path('home/pedido', views_pedio.pedido_list, name='pedido_list'),
    path('home/pedido', views_pedio.criar_pedido, name='criar_pedido'),


]
