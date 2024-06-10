from .models import Pedido
from django.shortcuts import render, redirect
from pedido.models import Pedido
from cliente.models import Cliente
from produto.models import Produto
from django.http import HttpResponse
from django.views.generic import ListView

class ListaPedidosView(ListView):
    model = Pedido
    template_name = 'list/list_pedido.html'
    context_object_name = 'pedidos'


def criar_pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produtos_ids = request.POST.getlist('produtos')
        cliente = Cliente.objects.get(cpf=cliente_id)
        produtos = Produto.objects.filter(pk__in=produtos_ids)
        novo_pedido = Pedido.objects.create(cliente=cliente)
        novo_pedido.produtos.set(produtos)
        novo_pedido.save()
        return redirect('macaco')

    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    return render(request, 'pedido/pedido.html', {'clientes': clientes, 'produtos': produtos})


def delet(request):
    cliente = Cliente.objects.all()
    cliente.delete()
    return render(request, 'list/list_pedido.html')