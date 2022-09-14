from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.
from apps.propietario.models import Propietario


class Marca(models.Model):
    Marca = models.CharField(max_length=35)
    def __str__(self):
        return  self.Marca

class Linea(models.Model):
    Linea = models.CharField(max_length=35)
    marca = models.ForeignKey(Marca, null=False, blank=False, on_delete=models.CASCADE)
    def __str__(self):
        return  self.Linea

class Color(models.Model):
    Color = models.CharField(max_length=35)
    def __str__(self):
        return  self.Color




class Vehiculo (models.Model):
    modelo = models.IntegerField(
        default=2018,
        validators=[MaxValueValidator(2018), MinValueValidator(1900)]
    )
    CLASES=((1, 'AUTOMÓVIL'),(2, 'BUS'),(3, 'BUSETA'),(4,' CAMIÓN'),(5, 'CAMIONETA'),(6, 'CAMPERO'),(7, 'MICROBÚS'),
            (8, 'TRACTOCAMIÓN'),(9, 'MOTOCICLETA'),(10, 'MOTOCARRO'),(11,' MOTOTRICICLO'),(12, 'CUATRIMOTO'),
            (13, 'VOLQUETA'),(14, 'OTRO'))
    clase =models.IntegerField(choices=CLASES,default=1)
    placa= models.CharField(max_length=6)
    color= models.ForeignKey(Color,null=False,blank=False,on_delete=models.CASCADE)
    marca= models.ForeignKey(Marca,null=False,blank=False,on_delete=models.CASCADE)
    linea= models.ForeignKey(Linea,null=False,blank=False,on_delete=models.CASCADE)
    MOTORES = (('V6', 'V6'), ('V8', 'V8'), ('V10', 'V10'), ('V12', ' V12'), ('V16', 'V16'))
    motor =models.CharField(choices=MOTORES,default='V6',max_length=2)
    propietario = models.ForeignKey(Propietario, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa







