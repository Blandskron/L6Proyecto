from django.db import models
from django.contrib.auth.models import User

class Venta(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad = models.IntegerField()
    cliente = models.CharField(max_length=100)
    producto = models.CharField(max_length=100)
