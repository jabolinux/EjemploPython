from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.vehiculo.views import VehiculoList, VehiculoCreate, VehiculoDelete, VehiculoUpdate, VehiculoSearch

app_name = "vehiculo"
urlpatterns = [
    url(r'^nuevo$', login_required(VehiculoCreate.as_view()), name='vehiculo_crear'),
    url(r'^listar/', login_required(VehiculoSearch.as_view()), name='vehiculo_listar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(VehiculoDelete.as_view()), name='vehiculo_eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(VehiculoUpdate.as_view()), name='vehiculo_editar'),
]