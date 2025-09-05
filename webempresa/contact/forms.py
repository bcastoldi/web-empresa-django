from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required = True) # label es como verbose_name en los modelos
    email = forms.EmailField(label="Email",required = True)
    content = forms.CharField(label="Contenido",required = True)
