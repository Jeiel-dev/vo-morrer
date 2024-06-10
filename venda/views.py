from django.shortcuts import render
from produto.models import Produto
from cliente.models import Cliente
from django.http import HttpResponse
from .models import Item




# def vendas_list(request):
#   return render(request, 'vendas/vendas.html')

def vendas_list(request):
    produtos = Produto.objects.all()
    return render(request, 'vendas/vendas.html', {'produtos': produtos})



def cad_venda(request):
  # lista os produtos e clientes na tela de cadastro
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    
    return render(request, 'cad_vendas/cad_vendas.html', {'produtos': produtos})

def salvar(request):
  item = Item()
  item.produto = request.POST.get('produto')
  item.quantidade = request.POST.get('quantidade')
  item.save()
  return render(request, 'cad_vendas/cad_vendas.html', {'produtos': item})