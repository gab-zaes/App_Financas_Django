from django.db import models

from datetime import datetime

class Transacoes(models.Model):
    banco_origem = models.CharField(max_length=150, null=False, blank=False)
    agencia_origem = models.CharField(max_length=100, null=False, blank=False)
    conta_origem = models.CharField(max_length=100, null=False, blank=False)
    banco_destino = models.CharField(max_length=150, null=False, blank=False)
    agencia_destino = models.CharField(max_length=100, null=False, blank=False)
    conta_destino = models.CharField(max_length=100, null=False, blank=False)
    valor_transacao = models.FloatField(null=False, blank=False)
    data_transacao = models.DateField(blank=False)


    def __str__(self):
        return f"Transação {self.id}: de {self.banco_origem} para {self.banco_destino} em {self.data_transacao}.\n\n Valor: R${self.valor_transacao}"


    def clean(self):
        ...