from django.db import models


class Moto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cilindradas = models.IntegerField()
    placa = models.CharField(max_length=8, 
        default = 'xxx-xxxx')

    def __unicode__(self):
        return self.modelo


class Cliente(models.Model):

    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=10)
    moto = models.ForeignKey(Moto)

    def __unicode__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=10)

    def __unicode__(self):
        return self.nome

class Peca(models.Model):
    nome = models.CharField(max_length=150)
    marca = models.CharField(max_length=100)
    preco = models.FloatField()
    disponibilidade = models.BooleanField()
    quantidade = models.IntegerField()

    def __unicode__(self):
        return self.nome

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente)
    funcionario = models.ForeignKey(Funcionario)
    data = models.DateTimeField(auto_now_add=True)
    valor_total = models.FloatField()

    def __unicode__(self):
        return self.cliente.nome


class Item(models.Model):
    venda = models.ForeignKey(Venda)
    peca = models.ForeignKey(Peca)
    quantidade = models.IntegerField()
    valor_unitario = models.FloatField()
    valor_total = models.FloatField()

    def __unicode__(self):
        return self.venda.cliente.nome


class Abastecedor(models.Model):
    nome = models.CharField(max_length=100)
    peca = models.ForeignKey(Peca)

    def __unicode__(self):
        return self.nome


class Compra(models.Model):
    funcionario = models.ForeignKey(Funcionario)
    abastecedor = models.ForeignKey(Abastecedor)
    quantidade = models.IntegerField()

    def __unicode__(self):
        return self.funcionario.nome