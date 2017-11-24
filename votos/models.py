# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
    votos_totales = models.IntegerField('Gente que fue a votar', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'DISTRITO'

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase

    Se decide elegir este modelo de datos ya que el desarrollador considera
    que se requieren los datos basicos del candidato (Nombre, Apellido) y al 
    partido politico que este represanta.
    """
    nombre = models.CharField('Nombre del Candidato', max_length=128)
    apellido = models.CharField('Apellido del Candidato', max_length=128)
    partido = models.CharField('Partido Politico al que pertenece el candidato', max_length=128)
    votos_obtenidos= models.IntegerField('Cantidad de Votos', default=0)
    
    def __str__(self):
        return 'Candidato {}'.format(self.nombre)

    class Meta:
        managed = True
        db_table = 'CANDIDATO'


class Votos(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase

    Se decide elegir este modelo de datos porque el desarrollador considera
    que los votos solo tienen los atributos para saber en que distrito se 
    efectuo el voto y para que candidato fue.
    """
    Distrito = models.ForeignKey(Distrito)
    Candidato = models.ForeignKey(Candidato)
    
    def __str__(self):
        return 'Voto por  {}'.format(self.Candidato.nombre)

    class Meta:
        managed = True
        db_table = 'VOTOS'
