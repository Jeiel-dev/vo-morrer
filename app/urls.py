
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('home.urls')),
    path('home/', include('cliente.urls')),
    path('home/', include('produto.urls')),
    path('home/', include('venda.urls')),
    path('home', include('pedido.urls'))
]
