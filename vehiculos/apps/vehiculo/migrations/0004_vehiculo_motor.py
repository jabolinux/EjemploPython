# Generated by Django 2.1.1 on 2018-09-24 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0003_auto_20180923_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='motor',
            field=models.CharField(choices=[('V6', 'V6'), ('V8', 'V8'), ('V10', 'V10'), ('V12', ' V12'), ('V16', 'V16')], default='V6', max_length=2),
        ),
    ]