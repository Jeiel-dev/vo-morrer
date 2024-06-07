from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cliente
from django.http.response import HttpResponse

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {'clientes': clientes})


@login_required
def cadastro(request):
    return render(request, 'cad_cliente/cad_cliente.html')


@login_required
def salvar(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        cliente = Cliente.objects.filter(cpf=cpf)

        if cliente:
            return HttpResponse('Já cadastrado')

        else:
            cliente = Cliente()
            cliente.nome = request.POST.get('nome')
            cliente.cpf = request.POST.get('cpf')
            cliente.cep = request.POST.get('cep')
            cliente.endereco = request.POST.get('endereco')
            cliente.data_nasc = request.POST.get('data_nasc')
            cliente.save()
            return redirect('clientes')  # Corrigido: redireciona para a lista de clientes
    else:
        return redirect('cadastro')  # Corrigido: redireciona para a página de cadastro se não for POST


@login_required
def home(request):
    return redirect('home:home')


def editar(request, cpf):
  cliente = Cliente.objects.get(cpf=cpf)
  return render(request, 'clientes/update.html', {'cliente':cliente})

def update(request, cpf):
  cliente = Cliente.objects.get(cpf=cpf)
  
  cliente.nome = request.POST.get('nome')
  cliente.cpf = request.POST.get('cpf')
  cliente.cep = request.POST.get('cep')
  cliente.endereco = request.POST.get('endereco')
  cliente.data_nasc = request.POST.get('data_nasc')
  cliente.save()
  return redirect('clientes')

def delet(request, cpf):
  cliente = Cliente.objects.get(cpf=cpf)
  cliente.delete()
  return redirect('clientes')
  