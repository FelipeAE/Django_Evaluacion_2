from django import forms
from Socios_APP.models import Socio
from django.core import validators

class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'fecha_incorporacion', 'fecha_nacimiento', 'telefono', 'correo_electronico', 'sexo', 'estado', 'observacion']
        labels = {
            'nombre': 'Nombre completo',
            'fecha_incorporacion': 'Fecha de incorporación',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'telefono': 'Teléfono',
            'correo_electronico': 'Correo electrónico',
            'sexo': 'Sexo',
            'estado': 'Estado',
            'observacion': 'Observación',
        }
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre completo'}),
        #     'fecha_incorporacion': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese fecha de incorporación', 'type': 'date', 'value': '2023-12-03'}),
        #     'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese fecha de nacimiento', 'type': 'date', 'value': '1996-11-12',}),
        #     'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese teléfono',}),
        #     'correo_electronico': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo electrónico', 'type': 'email', 'value': ' '}),
        #     'sexo': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Ingrese sexo',}),
        #     'estado': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Ingrese estado',}),
        #     'observacion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese observación',}),
        # }
    Estado = [('Vigente', 'Vigente'), ('Retirado', 'Retirado'), ('Suspendido', 'Suspendido')]
    
    nombre = forms.CharField(validators=[validators.MinLengthValidator(3, 'El nombre debe tener un mínimo de 3 caracteres'), validators.MaxLengthValidator(80, 'El nombre debe tener un máximo de 80 caracteres')], widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre completo'}))
    fecha_incorporacion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese fecha de incorporación', 'type': 'date', 'value': '2023-12-03'}))
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese fecha de nacimiento', 'type': 'date', 'value': '1996-11-12',}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese teléfono',}), validators=[validators.MinLengthValidator(9, 'El teléfono debe tener un mínimo de 9 caracteres'), validators.MaxLengthValidator(15, 'El teléfono debe tener un máximo de 15 caracteres')])
    correo_electronico = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo electrónico',}), validators=[validators.MinLengthValidator(10, 'El correo electrónico debe tener un mínimo de 10 caracteres'), validators.MaxLengthValidator(50, 'El correo electrónico debe tener un máximo de 50 caracteres')])
    sexo = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')], widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Ingrese sexo',}))
    estado = forms.ChoiceField(choices=Estado, widget=forms.Select(attrs={'class': 'form-select', 'placeholder': 'Ingrese estado',}))
    observacion = forms.CharField(required=False ,widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese observación',}))
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     fecha_incorporacion = cleaned_data.get('fecha_incorporacion')
    #     fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
    #     if fecha_incorporacion and fecha_nacimiento:
    #         if fecha_incorporacion < fecha_nacimiento:
    #             raise forms.ValidationError('La fecha de incorporación debe ser mayor a la fecha de nacimiento')
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if not all(x.isalpha() or x.isspace() for x in nombre):
            raise forms.ValidationError('El nombre solo puede contener letras y espacios')
        return nombre

    
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        if not telefono.isdigit():
            raise forms.ValidationError('El teléfono solo puede contener números')
        return telefono
    
    def clean_correo_electronico(self):
        correo_electronico = self.cleaned_data['correo_electronico']
        if "@" not in correo_electronico:
            raise forms.ValidationError('El correo electrónico debe contener un @')
        return correo_electronico
    
    def clean_fecha_incorporacion(self):
        fecha_incorporacion = self.cleaned_data['fecha_incorporacion']
        if fecha_incorporacion.year < 2020:
            raise forms.ValidationError('La fecha de incorporación debe ser mayor a 2020')
        return fecha_incorporacion
    
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        if fecha_nacimiento.year < 1900 or fecha_nacimiento.year > 2023:
            raise forms.ValidationError('La fecha de nacimiento debe ser mayor a 1900 y menor a 2023')
        return fecha_nacimiento
    
    
    
    