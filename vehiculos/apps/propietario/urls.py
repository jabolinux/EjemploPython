from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.propietario.views import PropietarioCreate, PropietarioList, PropietarioDelete, PropietarioUpdate

app_name = "propietario"
urlpatterns = [
    url(r'^nuevo$', (PropietarioCreate.as_view()), name='propietario_crear'),
    url(r'^listar', (PropietarioList.as_view()), name='propietario_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(PropietarioUpdate.as_view()), name='propietario_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', (PropietarioDelete.as_view()),name='propietario_eliminar'),
]