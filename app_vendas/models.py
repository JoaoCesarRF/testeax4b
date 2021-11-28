from django.db import models


class Cliente(models.Model):
    cod_cliente = models.IntegerField(primary_key=True, blank=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    email = models.EmailField(default=None)
    whats = models.BooleanField(default=None)
    telefone = models.CharField(max_length=15)

    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    cod_produto = models.IntegerField(primary_key=True, blank=True)
    titulo = models.CharField(max_length=20, default='Titulo')
    descricao_produto = models.TextField(default='Descreva o Produto')
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, unique=True)

    def __str__(self):
        return self.titulo


class Venda(models.Model):
    cod_venda = models.IntegerField(primary_key=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ForeignKey(Produto, on_delete=models.CASCADE)
    observacao = models.TextField(default=None, blank=True)

    class TipoPagamento(models.TextChoices):
        visa = 'VIsa', 'Visa'
        boleto = 'Boleto', 'Boleto'
        master = 'Mastercard', 'Mastercard'

    tipo_pagamento = models.CharField(max_length=10, choices=TipoPagamento.choices, default='Visa',
                                      verbose_name='Meio de Pagamento')

    def __str__(self):
        return self.cod_venda.__str__()