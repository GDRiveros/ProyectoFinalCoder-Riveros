from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogFormulario(forms.Form):

    titulo = forms.CharField()
    subtitulo = forms.IntegerField()
    autor = forms.CharField()
    cuerpo = forms.IntegerField()
    fecha = forms.DateField()

class UserEditionForm(UserCreationForm):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label= "Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ["username","email", "password1", "password2", "first_name", "last_name"]
        help_texts = { k: "" for k in fields}

from BlogCoder.models import Avatar

class AvatarForm(forms.ModelForm):

    imagen = forms.ImageField()

    class Meta:
        model = Avatar
        fields = ["imagen", "user"]
