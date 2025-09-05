from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage # sirve para crear la estructura d eun mensaje e incluye un metodo para enviarlo
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm() # primero lo creamos

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST) # luego si es que se enviaron datos por POST, rellenamos la plantilla con esa informacion 
        if contact_form.is_valid(): 
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos

            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\n{}".format(name, email, content), #cuerpo
                "no-contestar@inbox.mailtrap.io", #email_origen
                ["bcastoldi@bancocredicoop.coop"], #email_destino
                reply_to = [email] # el email que capturamos del port
            )
            try:
                email.send()
                # todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except Exception as e:
                # algo no ha ido bien, redireccionamos a FAIL
                print(e)
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form': contact_form})
