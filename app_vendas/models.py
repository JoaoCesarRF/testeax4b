from django.db import models


class Venda(models.Model):
    cod_venda = models.IntegerField(primary_key=True, blank=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    produtos = models.ForeignKey('Produto', on_delete=models.CASCADE)
    observacao = models.TextField()
    def __str__(self):
        return self.cod_venda

class Cliente(models.Model):
    cod_cliente = models.IntegerField(primary_key=True, blank=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    whats = models.BooleanField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    cod_produto = models.IntegerField(primary_key=True, blank=True)
    titulo = models.CharField(max_length=15)
    descricao_produto = models.TextField()
    preco = models.DecimalField(max_digits=7,decimal_places=2)
    def __str__(self):
        return self.titulo
