from django.urls import path
from . import views
from login import views as views_login

urlpatterns = [
    # url: .../cadastro
    # path(views.home, name='home'),
    # path('home-/', views.home, name='init')
    path('logout/', views.logout, name='logout')

]
