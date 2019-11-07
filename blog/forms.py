from django import forms

from .models import Entrada

class AutorForm(forms.Form):
	nombres=forms.CharField(label='Nombres: ',max_length=80)
	apellidos=forms.CharField(label='Apellidos: ',max_length=80)

class EntradaForm(forms.ModelForm):
	class Meta:
		model=Entrada
		exclude =['id_entrada','fecha_hora']