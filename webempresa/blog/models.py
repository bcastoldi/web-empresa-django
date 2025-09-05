from django.db import models
from django.utils.timezone import now # detectara la zona horaria donde esta creado el proyecto
from django.contrib.auth.models import User #MODELO DE USUARIOS contiene todos los usuarios que estan registrados en nuestro panel de administrador

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=100, verbose_name="Nombre")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural= "categorias"
        ordering=['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido") # es obligatorio, por eso no le ponemos blank ni null
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now) # accedemos a la hora actual
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null = True, blank= True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete= models.CASCADE) #es obligatoria la variable on_delete, que lo que hace es indicarle a Django que hacer si se elimina el Usuario (ya que estan relacionados mediante foreign key). En este caso, cascade elimina a todos los modelos que hayan sido creados por este autor
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural= "entradas"
        ordering=['-created']

    def __str__(self):
        return self.title

#TODO: solucionar problema con el atraso del horario del servidor