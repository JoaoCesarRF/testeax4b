from django.forms import ModelForm
from .models import Venda, Cliente, Produto


class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'produtos', 'observacao']


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'email', 'whats', 'telefone']


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['titulo', 'descricao_produto', 'preco']
