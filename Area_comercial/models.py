from django.db import models

#Creacion de tablas
class Notas(models.Model):
    titulo = models.CharField(max_length=200,null=True)
    descripcion = models.CharField(max_length=200,null=True)
    fecha = models.DateTimeField(null=True)
    
    
    
class Empresa(models.Model):
    Nombre_empresa = models.CharField(max_length=200)
    Nuevo = models.CharField(max_length=200,null=True)
    Encargado = models.CharField(max_length=200,default=0)
    Telefono = models.CharField(max_length=200, default=0)
    Email = models.CharField(max_length=200, default=0)
    notas = models.ForeignKey(Notas,on_delete=models.CASCADE,null = True)

# crea

         
# Tabla de Empresa
class Ofertas(models.Model):
 Mes = models.CharField(max_length=200,null=True)
 Cliente = models.ForeignKey(Empresa,on_delete=models.CASCADE,null=True,default=0)
 Descripcion = models.CharField(max_length=200,null=True)
 Estado = models.CharField(max_length=200,null=True)
 Pago_mensual = models.CharField(max_length=200,null=True)
 Por_campaña = models.CharField(max_length=200,default=0,null=True)
 Sector = models.CharField(max_length=200,null=True)   
 Canal_medio = models.CharField(max_length=200, default='l',null=True)
 Causal_negacion = models.CharField(max_length=200,null=True)    
 Anio  = models.CharField(max_length=200,null=True)  
 
 