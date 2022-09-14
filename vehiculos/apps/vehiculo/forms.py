from django import forms

from apps.vehiculo.models import Vehiculo

class VehiculoForm(forms.ModelForm):
	class Meta:
		model = Vehiculo

		fields = [
			'placa',
			'clase',
			'modelo',
			'marca',
			'linea',
			'color',
			'motor',
			'propietario',
		]
		labels = {
			'placa':'Placa',
			'clase':'Clase',
			'modelo':'Modelo',
			'marca':'Marca',
			'linea':'Linea',
			'motor':'Motor',
			'color':'Color',
			'propietario':'Propietario',
		}
		widgets = {
			'placa': forms.TextInput(attrs={'class':'form-control'}),
			'propietario': forms.Select(attrs={'class': 'form-control'}),
			'color': forms.Select(attrs={'class': 'form-control'}),
			'clase': forms.Select(attrs={'class': 'form-control'}),
			'modelo': forms.TextInput(attrs={'class': 'form-control'}),
			'marca': forms.Select(attrs={'class': 'form-control'}),
			'linea': forms.Select(attrs={'class': 'form-control'}),
			'motor': forms.Select(attrs={'class': 'form-control'}),
		}


