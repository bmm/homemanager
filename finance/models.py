from django.db import models
from django.db.models import Sum

class Entidade(models.Model):
    nome = models.CharField(max_length=100)
    nif = models.CharField(max_length=50)
    morada = models.CharField(max_length=200)
    
class Fatura(models.Model):
    entidade = models.ForeignKey(Entidade)
    data = models.DateField()

class LinhaFatura(models.Model):
    fatura = models.ForeignKey(Fatura)
    iva = models.FloatField(default=0)
    valor = models.FloatField(default=0)

class Despesa(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_length=200)
    pago = models.BooleanField()
    # periodicidade

class ContaBancaria(models.Model):
    nome = models.CharField(max_length=50)

    def saldo(self):
        return MovimentoBancario.objects.filter(conta=self).aggregate(Sum('montante'))

    def __unicode__(self):
        return self.nome

class MovimentoBancario(models.Model):
    conta = models.ForeignKey(ContaBancaria)
    data_valor = models.DateField()
    data_movimento = models.DateField()
    descricao = models.CharField(max_length=200)
    montante = models.FloatField(default=0)

class Receita(models.Model):
    entidade = models.ForeignKey(Entidade)
    valor = models.FloatField(default=0)
    # periodicidade
     
