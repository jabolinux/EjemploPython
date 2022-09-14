from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Propietario(models.Model):
    TIPOS_DOCUMENTO=(('CC' , 'Cédula de Ciudadanía'),
                   ('CE' , 'Cédula de extranjería'),
                   ('PB' , 'Pasaporte'),
                   ('TI' , 'Tarjeta de identidad'),
                   ('NI' , 'NIT'))
    Email = models.EmailField(null=True)
    Celular_Regex = RegexValidator(regex=r'\d{3}-\d{7}-\d',
                                 message="El formato del celular debe ser: '999-9999999'. maximo 10 digitos")
    Celular = models.CharField(validators=[Celular_Regex], max_length=17, blank=True)
    TipoDocumento = models.CharField(choices=TIPOS_DOCUMENTO, default='CC',max_length=2)
    NumeroDocumento = models.CharField(max_length=12)
    PrimerApellido = models.CharField(max_length=35)
    SegundoApellido = models.CharField(max_length=35)
    PrimerNombre = models.CharField(max_length=35)
    SegundoNombre = models.CharField(max_length=35)
    FechaNacimiento = models.DateField(null=True)
    GENEROS=(('M','Masculino'),('F','Femenino'))
    Genero = models.CharField(choices=GENEROS, default='M',max_length=1)


    def NombreCompleto(self):
        cadena='{0} {1} {2} {3}'
        return cadena.format(self.PrimerApellido,self.SegundoApellido,self.PrimerNombre,self.SegundoNombre)
    def __str__(self):
        return  self.NombreCompleto()
