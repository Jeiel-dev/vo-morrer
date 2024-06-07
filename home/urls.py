from django.urls import path
from . import views
from cliente import views as views_cliente

urlpatterns = [
    # url: .../cadastro
    # path(views.home, name='home'),
    # path('home-/', views.home, name='init')
    path('logout/', views.logout, name='logout'),
    path('home/cadastro/', views_cliente.cadastro, name='cad_cliente'),
    path('home/clientes/', views_cliente.lista_clientes, name='clientes'),

]
