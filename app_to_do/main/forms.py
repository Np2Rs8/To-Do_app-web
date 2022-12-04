from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from ckeditor.fields import RichTextField

from .models import TaskModel

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username','email','password1','password2']



class TaskForm(forms.ModelForm):

	titulo = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'id': 'titulo',
			'name': 'titulo',
			'placeholder': '*Titulo...',
		}))

	descripcion = forms.CharField(max_length=1000, required=True,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'id': 'descripcion',
			'name': 'descripcion',
			'placeholder': '*Descripcion...',
		}))

	categoria = [
		('Incompleto', 'Incompleto'),
		('Proceso', 'Proceso'),
		('Completado', 'Completado')
	]

	estado = forms.ChoiceField(choices=categoria,
		widget=forms.RadioSelect(attrs={
			'type': 'radio',
			'class': 'form-control',
			'id': 'estado',
			'name': 'estado',
		}))

	cuerpo = RichTextField()

	class Meta:
		
		model = TaskModel
		fields = ('titulo', 'descripcion', 'estado', 'cuerpo')

