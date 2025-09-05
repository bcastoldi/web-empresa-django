from django import template # registrarlo dentro de la libreria de templates
from pages.models import Page # importar nuestro modelo de paginas

register = template.Library() # L mayuscula!!

@register.simple_tag
def get_page_list():
    pages = Page.objects.all() # recuperar todas las paginas
    return pages 

# transformamos una funcion normal en un tag simple y lo registramos en la libreria de template

# una vez completado, es importante reiniciar el servidor para que incluya estos nuevos template tags en la memoria

