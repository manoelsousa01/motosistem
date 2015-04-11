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
