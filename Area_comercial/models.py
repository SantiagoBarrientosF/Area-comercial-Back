from django.db import models

#Creacion de tablas

# Tabla de Empresa
class Empresa(models.Model):
 Nombre = models.CharField(max_length=200)
 Nuevo = models.CharField(max_length=200)
 Sector = models.CharField(max_length=200)
 Licitacion_id = models.ForeignKey("Licitacion",on_delete=models.CASCADE)
 Canal = models.CharField(max_length=200)
 Contacto_id = models.ForeignKey("Contacto",on_delete=models.CASCADE)
    
    
    
    
# Tabla de Licitacion    
class Licitacion(models.Model):
    Servicio = models.CharField(max_length=200)
    Descripcion = models.CharField(max_length=200)
    Estado = models.CharField(max_length=200)
    Cobro_id = models.ForeignKey("Cobro",on_delete=models.CASCADE)
    Causa_negacion = models.CharField(max_length=200)
    Nota_id = models.ForeignKey("Notas",on_delete=models.CASCADE)
    
    
# Tabla de Cobro   
class Cobro(models.Model):
    Monto = models.IntegerField
    Campaña = models.CharField(max_length=200)
   

# Tabla de Contacto     
class Contacto(models.Model):
    Encargado = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=200)
    Correo = models.CharField(max_length=200)
   

# Tabla de Notas     
class Notas(models.Model):
    Descripcion = models.CharField(max_length=200)
    
    
    

   


