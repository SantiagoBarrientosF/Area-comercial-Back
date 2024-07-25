from django.db import models

#Creacion de tablas

# Tabla de Empresa
class Ofertas(models.Model):
 Mes = models.CharField(max_length=200)
 Cliente = models.CharField(max_length=200,default=0)
 Nuevo = models.CharField(max_length=200)
 Descripcion = models.CharField(max_length=200)
 Estado = models.CharField(max_length=200)
 Pago_mensual = models.CharField(max_length=200)
 Por_campaña = models.CharField(max_length=200,default=0)
 Sector = models.CharField(max_length=200)   
 Canal_medio = models.CharField(max_length=200, default='l')
 Causal_negacion = models.CharField(max_length=200)   
 Observaciones = models.CharField(max_length=200,default=0)   

class Empresa(models.Model):
    Nombre_empresa = models.CharField(max_length=200)
    Encargado = models.CharField(max_length=200,default=0)
    Telefono = models.CharField(max_length=200, default=0)
    Email = models.CharField(max_length=200, default=0)