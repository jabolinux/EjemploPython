# Generated by Django 2.1.1 on 2018-09-24 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propietario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietario',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='propietario',
            name='FechaNacimiento',
            field=models.DateField(null=True),
        ),
    ]