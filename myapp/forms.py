from django import forms
from .models import Proyecto, Lista, Tarea


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion']


class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ['nombre', 'proyecto']


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'lista']