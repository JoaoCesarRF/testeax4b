from django.shortcuts import redirect
from django.shortcuts import render
from django.db import models
from .form import VendaForm, ClienteForm, ProdutoForm
from .models import Venda, Cliente, Produto


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    dados = {}
    dados['vendas'] = Venda.objects.all()
    return render(request, 'dashboard.html', dados)
# criar dashboard de cleintes e Produtos


def vendas_update(request, pk):
    dados = {}
    venda_dados = Venda.objects.get(pk=pk)
    venda = VendaForm(request.POST or None, instance=venda_dados)
    dados['venda'] = venda
    if venda.is_valid():
        venda.save()
        return redirect('dashboard')
    return render(request, 'venda_form.html', dados)


def nova_venda(request):
    dados = {}
    venda = VendaForm(request.POST or None)
    dados['venda'] = venda
    if venda.is_valid():
        venda.save()
        return redirect('dashboard')
    return render(request, 'venda_form.html', dados)


def cadastro_cliente(request):
    dados = {}
    cliente = ClienteForm(request.POST or None)
    dados['cliente'] = cliente
    if cliente.is_valid():
        cliente.save()
        return redirect('dashboard')
    return render(request, 'cliente_form.html', dados)


def dashboard_clientes(request):
    dados = {}
    dados['clientes'] = Cliente.objects.all()
    return render(request, 'dashboard_clientes.html', dados)

def clientes_update(request, pk):
    dados = {}
    cliente_dados = Cliente.objects.get(pk=pk)
    cliente = ClienteForm(request.POST or None, instance=cliente_dados)
    dados['cliente'] = cliente
    if cliente.is_valid():
        cliente.save()
        return redirect('dashboard')
    return render(request, 'cliente_form.html', dados)


def cadastro_produto(request):
    dados = {}
    produto = ProdutoForm(request.POST or None)
    dados['produto'] = produto
    if produto.is_valid():
        produto.save()
        return redirect('dashboard')
    return render(request, 'produto_form.html', dados)


def dashboard_produtos(request):
    dados = {}
    dados['produtos'] = Produto.objects.all()
    return render(request, 'dashboard_produtos.html', dados)

def produtos_update(request, pk):
    dados = {}
    produto_dados = Produto.objects.get(pk=pk)
    produto = ProdutoForm(request.POST or None, instance=produto_dados)
    dados['produto'] = produto
    if produto.is_valid():
        produto.save()
        return redirect('dashboard')
    return render(request, 'produto_form.html', dados)
