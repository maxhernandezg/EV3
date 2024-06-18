from django import forms
from .models import Genero

from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        # hace referencia a “todos” los campos
        #fields = "__all__"
        fields = ["genero",]
        labels = {'genero' : "Género"}