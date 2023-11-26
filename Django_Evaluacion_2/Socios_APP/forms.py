from django import forms
from django.core import validators

class SocioForm(forms.Form):
    ESTADOS = [
        ('Vigente', 'Vigente'), 
        ('Suspendido', 'Suspendido'), 
        ('Retirado', 'Retirado')
    ]
    
    nombre = forms.CharField(
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(80)
        ]
    )
    fecha_incorporacion = forms.DateField()
    año_nacimiento = forms.DateField()
    telefono = forms.CharField(required=False, max_length=100)
    email = forms.EmailField()  
    sexo = forms.ChoiceField(choices=(('M', 'Masculino'), ('F', 'Femenino')), widget=forms.RadioSelect)
    estado = forms.ChoiceField(choices=ESTADOS, widget=forms.Select)
    observacion = forms.CharField(required=False, widget=forms.Textarea)  
    
    def __init__(self, *args, **kwargs):
        super(SocioForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['fecha_incorporacion'].widget.attrs.update({'class': 'form-control'})
        self.fields['año_nacimiento'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['sexo'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['estado'].widget.attrs.update({'class': 'form-select'})
        self.fields['observacion'].widget.attrs.update({'class': 'form-control'})

    # def clean(self):
    #     cleaned_data = super().clean()
    #     # Aquí puedes incluir cualquier validación personalizada que afecte a múltiples campos
    #     return cleaned_data
    
    def clean_email(self):
        input_email = self.cleaned_data.get('email')
        if input_email and '@' not in input_email:
            raise forms.ValidationError('El email debe contener un @')
        return input_email
