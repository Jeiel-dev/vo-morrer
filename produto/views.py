from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Produto
from django.http.response import HttpResponse

# Create your views here.


def cadastro_produto(request):
    return render(request, 'cad_produto/cad_produto.html')





def produtos_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/produto.html', {'produtos': produtos})


def salvar_p(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        produto = Produto.objects.filter(cod_barra=codigo)

        if produto:
            return HttpResponse('Ja cadastrado')

        else:
            produto = Produto()
            produto.cod_barra = request.POST.get('codigo')
            produto.nome = request.POST.get('nome')
            produto.descricao = request.POST.get('descricao')
            produto.valor = request.POST.get('valor')
            produto.save()
            return redirect('produtos')

    else:
        return redirect('cad_produtos')


def editar_p(request, cod_barra):
    produto = Produto.objects.get(cod_barra=cod_barra)
    return render(request, 'produto/update.html', {'produto': produto})


def update(request, cod_barra):
    produto = Produto.objects.get(cod_barra=cod_barra)
    
    produto.cod_barra = request.POST.get('cod_barra')
    produto.nome = request.POST.get('nome')
    produto.descricao = request.POST.get('descricao')
    produto.valor = request.POST.get('valor')
    produto.save()
    
    return redirect('pruduto_list')


def deletar_p(request, cod_barra):
    produto = Produto.objects.get(cod_barra=cod_barra)
    produto.delete()
    return redirect('pruduto_list')
