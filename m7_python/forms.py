from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre')
    first_name.label = 'Nombre'
    last_name = forms.CharField(label='Apellido')
    last_name.label = 'Apellido'
    email = forms.EmailField(label='Correo')
    email.label = 'Correo'

    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        labels = {'username': _("Nombre de usuario")}


class TipoForm(forms.Form):
    tipos = ((1, 'Arrendatario'), (2, 'Arrendador'),)
    tipo = forms.ChoiceField(label='Tipo', choices=tipos)
    rut = forms.CharField(label='Rut', max_length=100)
    direccion = forms.CharField(label='Dirección', max_length=100)
    telefono = forms.CharField(label='Teléfono', max_length=100)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
