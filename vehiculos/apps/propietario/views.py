from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.propietario.forms import PropietarioForm
from apps.propietario.models import Propietario

class PropietarioList(ListView):
    model = Propietario
    template_name = 'propietario/propietario_list.html'
    paginate_by = 7

class PropietarioCreate(CreateView):
	model = Propietario
	form_class = PropietarioForm
	template_name = 'propietario/propietario_form.html'
	success_url = reverse_lazy('propietario:propietario_listar')


class PropietarioUpdate(UpdateView):
	model = Propietario
	form_class = PropietarioForm
	template_name = 'propietario/propietario_form.html'
	success_url = reverse_lazy('propietario:propietario_listar')


class PropietarioDelete(DeleteView):
	model = Propietario
	template_name = 'propietario/propietario_delete.html'
	success_url = reverse_lazy('propietario:propietario_listar')