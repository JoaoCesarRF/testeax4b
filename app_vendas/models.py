from django.db import models


class Venda(models.Model):
    cod_venda = models.CharField(max_length=5, auto_created=True, primary_key=True, blank=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    produtos = models.ForeignKey('Produto', on_delete=models.CASCADE)


class Cliente(models.Model):
    cod_cliente = models.CharField(max_length=5, auto_created=True, primary_key=True, blank=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    email = models.EmailField
    telefone = models.CharField(max_length=15)
    whatss = models.BooleanField
    data_cadastro = models.DateTimeField(auto_now_add=True)


class Produto(models.Model):
    cod_produto = models.CharField(max_length=5, auto_created=True, primary_key=True, blank=True)
    descricao_produto = models.CharField(max_length=100)
    preco = models.IntegerField
