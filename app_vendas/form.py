from django.forms import ModelForm
from .models import Venda, Cliente, Produto


class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['cod_venda', 'cliente', 'produtos', 'observacao','tipo_pagamento']


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'email', 'whats', 'telefone']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo', 'descricao_produto', 'preco']

