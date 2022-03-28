
from django.db import models



class Cypto(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()
    tir = models.IntegerField()

class Cedear(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()
    tir = models.IntegerField()

class opcionNegociable(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()
    tir = models.IntegerField()

class FCI(models.Model):
    nombre=models.CharField(max_length=40)
    precio = models.IntegerField()
    tir = models.IntegerField()