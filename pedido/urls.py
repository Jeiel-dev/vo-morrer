from django.urls import path
from . import views
from .views import ListaPedidosView

urlpatterns = [
  path('lista_pedidos/', ListaPedidosView.as_view(), name='lista_pedido'),
  path('lista_pedidos/', ListaPedidosView.as_view(), name='macaco'),
  path('delet/', views.delet, name='delet_list')
]
