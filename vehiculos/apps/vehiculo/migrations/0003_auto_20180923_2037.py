# Generated by Django 2.1.1 on 2018-09-23 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propietario', '0001_initial'),
        ('vehiculo', '0002_auto_20180923_1948'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Propietario',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='propietario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='propietario.Propietario'),
        ),
    ]
