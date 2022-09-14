from django.contrib import admin


# Register your models here.
from apps.vehiculo.models import Marca, Color, Linea

admin.site.register(Marca)
admin.site.register(Color)
admin.site.register(Linea)


