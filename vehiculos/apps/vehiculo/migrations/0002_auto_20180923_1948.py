# Generated by Django 2.1.1 on 2018-09-23 19:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietario',
            name='Celular',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="El formato del celular debe ser: '999-9999999'. maximo 10 digitos", regex='\\d{3}-\\d{7}-\\d')]),
        ),
        migrations.AddField(
            model_name='propietario',
            name='Genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='propietario',
            name='TipoDocumento',
            field=models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de extranjería'), ('PB', 'Pasaporte'), ('TI', 'Tarjeta de identidad'), ('NI', 'NIT')], default='CC', max_length=2),
        ),
    ]
