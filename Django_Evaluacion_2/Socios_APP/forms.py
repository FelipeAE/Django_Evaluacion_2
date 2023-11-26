from django import forms
from Socios_APP.models import Socio
from django.core import validators

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre completo'
                }
            ),
            'fecha_incorporacion': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese fecha de incorporación'
                }
            ),
            'fecha_nacimiento': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese fecha de nacimiento'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese teléfono'
                }
            ),
            'correo_electronico': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese correo electrónico'
                }
            ),
            'sexo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese sexo'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese estado'
                }
            ),
            'observacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese observación'
                }
            ),
        }
        labels = {
            'nombre': 'Nombre',
            'fecha_incorporacion': 'Fecha de incorporación',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'telefono': 'Teléfono',
            'correo_electronico': 'Correo electrónico',
            'sexo': 'Sexo',
            'estado': 'Estado',
            'observacion': 'Observación',
        }
        error_messages = {
            'nombre': {
                'required': 'El nombre es requerido'
            },
            'fecha_incorporacion': {
                'required': 'La fecha de incorporación es requerida'
            },
            'fecha_nacimiento': {
                'required': 'La fecha de nacimiento es requerida'
            },
            'telefono': {
                'required': 'El teléfono es requerido'
            },
            'correo_electronico': {
                'required': 'El correo electrónico es requerido'
            },
            'sexo': {
                'required': 'El sexo es requerido'
            },
            "estado": {
                "required": "El estado es requerido"
            }}