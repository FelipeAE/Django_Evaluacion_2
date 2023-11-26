from django.db import models

class Socio(models.Model):
    ESTADOS = (
        ('Vigente', 'Vigente'),
        ('Suspendido', 'Suspendido'),
        ('Retirado', 'Retirado'),
    )

    nombre = models.CharField(max_length=80)
    fecha_incorporacion = models.DateField()
    año_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    sexo = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')))
    estado = models.CharField(max_length=10, choices=ESTADOS)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
