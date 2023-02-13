from django.db import models
from datetime import date
from users.models import User


class Salas(models.Model):
    name = models.CharField(max_length=30)
    tam = models.DecimalField(max_digits=3, decimal_places=0)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Sala'
        

class Eventos(models.Model):
    name = models.CharField(max_length=80, verbose_name= 'Disciplina ou Tema:')
    registrationDate = models.DateField(default= date.today, verbose_name= 'Data')
    timeStart = models.TimeField( verbose_name= 'Hora inicial')
    timeEnd = models.TimeField(verbose_name= 'Hora final')
    meals = models.DecimalField(max_digits=3, decimal_places= 0, verbose_name= 'Refeições')
    tipo = models.CharField(max_length=12)
    #gerando uma key para as salas se conectarem aos eventos
    local = models.ForeignKey(Salas, on_delete= models.DO_NOTHING, verbose_name= 'Local')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Evento'
