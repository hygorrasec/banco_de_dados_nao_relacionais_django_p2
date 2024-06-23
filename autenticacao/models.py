from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateTimeField('data do evento')

    def __str__(self):
        return self.nome
