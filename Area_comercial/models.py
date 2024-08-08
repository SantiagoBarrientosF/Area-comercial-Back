from django.db import models

#Creacion de tablas
class Empresa(models.Model):
    Nombre_empresa = models.CharField(max_length=200)
    Encargado = models.CharField(max_length=200,default=0)
    Telefono = models.CharField(max_length=200, default=0)
    Email = models.CharField(max_length=200, default=0)
# crea
class Notas(models.Model):
    notas = models.CharField(max_length=200)
         
# Tabla de Empresa
class Ofertas(models.Model):
 Mes = models.CharField(max_length=200)
 Cliente = models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,default=0)
 Nuevo = models.CharField(max_length=200)
 Descripcion = models.CharField(max_length=200)
 Estado = models.CharField(max_length=200)
 Pago_mensual = models.CharField(max_length=200)
 Por_campaña = models.CharField(max_length=200,default=0,null=True)
 Sector = models.CharField(max_length=200)   
 Canal_medio = models.CharField(max_length=200, default='l')
 Causal_negacion = models.CharField(max_length=200)      
 notas = models.ForeignKey(Notas,on_delete=models.CASCADE,null = True)
 
 