# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
#from votos.models import Votos as Votos
# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase

    Se decide modelar asi esta clase porque es necesario el nombre del candidato
     y la cantidad de votos que tuvo
    """
    nombre = models.CharField(max_length=128)
    distrito = models.ForeignKey(Distrito)
    


class Votos(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase

    Se decide modelar asi esta clase porque es necesario el voto por distrito(que seria el maximo de votos)
     y votos_nulos para poner la cantidad de votos nulo que a habido en el districto
    """
    votos_distrito = models.ManyToManyField(Distrito)
    porcentaje = models.IntegerField()
    votos_nulos = models.IntegerField()
    
    

    
