from builtins import object

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.vehiculo.forms import VehiculoForm
from apps.vehiculo.models import Vehiculo
from django.db.models import Q

class VehiculoList(ListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'
    paginate_by = 7


class VehiculoSearch(ListView):
	model = Vehiculo
	template_name = 'vehiculo/vehiculo_list.html'
	paginate_by = 7
	def get_queryset(self):
		p_placa=self.request.GET.get('placa')
		p_propietario=self.request.GET.get('propietario')
		p_cedula=self.request.GET.get('cedula')
		print(p_placa)
		print(p_cedula)
		print(p_propietario)
		if ((p_placa is not None and p_placa) or (p_propietario is not None and p_propietario) or (p_cedula is not None and p_cedula)):
			return super(VehiculoSearch, self).get_queryset().filter(Q(placa=p_placa) | \
				Q(propietario__PrimerApellido__icontains=p_propietario) | \
				Q(propietario__SegundoApellido__icontains=p_propietario) | \
				Q(propietario__SegundoNombre__icontains=p_propietario) | \
				Q(propietario__PrimerNombre__icontains=p_propietario) | \
				Q(propietario__NumeroDocumento=p_cedula)).order_by('placa')
		else:
			return super(VehiculoSearch, self).get_queryset()
class VehiculoCreate(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo:vehiculo_listar')


class VehiculoUpdate(UpdateView):
	model = Vehiculo
	form_class = VehiculoForm
	template_name = 'vehiculo/vehiculo_form.html'
	success_url = reverse_lazy('vehiculo:vehiculo_listar')


class VehiculoDelete(DeleteView):
	model = Vehiculo
	template_name = 'vehiculo/vehiculo_delete.html'
	success_url = reverse_lazy('vehiculo:vehiculo_listar')