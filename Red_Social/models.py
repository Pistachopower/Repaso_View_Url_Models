from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo_Electronico = models.TextField()
    contrasena= models.CharField(max_length=15)
    fecha_Registro= models.DateTimeField(default=timezone.now)
    biografia= models.CharField(max_length=200)
    foto_Perfil= models.TextField()
    
class  Publicacion(models.Model):
    titulo= models.CharField(max_length=200)
    contenido= models.CharField(max_length=200)
    fecha_Creacion= models.DateTimeField(default=timezone.now)
    autor= models.CharField(max_length=200)
    usuario= models.ForeignKey(Usuario, on_delete = models.CASCADE)
    
class  Comentario(models.Model):
    contenido= models.CharField(max_length=200)
    fecha_Creacion= models.DateTimeField(default=timezone.now)
    autor= models.CharField(max_length=200)
    usuario=  models.ForeignKey(Usuario, on_delete = models.CASCADE)
    publicacion= models.ForeignKey(Publicacion, on_delete = models.CASCADE)
    
    
class  Me_Gusta(models.Model):
    publicacion= models.CharField(max_length=200)
    usuario= models.ForeignKey(Usuario, on_delete = models.CASCADE)

class Seguidores(models.Model):  
    seguidor= models.CharField(max_length=200)
    seguido= models.CharField(max_length=200)
    usuario= models.ManyToManyField(Usuario)