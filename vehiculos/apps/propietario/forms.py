from django import forms

from apps.propietario.models import Propietario

BIRTH_YEAR_CHOICES = range(1900,2001)

class PropietarioForm(forms.ModelForm):

	class Meta:
		model = Propietario

		fields = [
            'TipoDocumento',
            'NumeroDocumento',
            'PrimerApellido',
            'SegundoApellido',
            'PrimerNombre',
            'SegundoNombre',
            'FechaNacimiento',
            'Genero',
            'Email',
            'Celular',
        ]
		labels = {
            'TipoDocumento': 'Tipo de documento',
            'NumeroDocumento': 'Número de documento',
            'PrimerApellido': 'Primer apellido',
            'SegundoApellido': 'Segundo apellido',
            'PrimerNombre': 'Primer nombre',
            'SegundoNombre': 'Segundo nombre',
            'FechaNacimiento': 'Fecha de nacimiento',
            'Genero': 'Genero',
            'Email': 'Correo electrónico',
            'Celular': 'Celular',
		}
		widgets = {
			'TipoDocumento': forms.Select(),
            'NumeroDocumento': forms.TextInput(attrs={'class': 'form-control'}),
            'PrimerApellido': forms.TextInput(attrs={'class':'form-control'}),
			'SegundoApellido': forms.TextInput(attrs={'class':'form-control'}),
			'PrimerNombre': forms.TextInput(attrs={'class':'form-control'}),
			'SegundoNombre': forms.TextInput(attrs={'class':'form-control'}),
            'FechaNacimiento': forms.SelectDateWidget(attrs={'class': 'datepicker'}, years=BIRTH_YEAR_CHOICES),
            'Genero': forms.TextInput(attrs={'class': 'form-control'}),
            'Celular': forms.TextInput(attrs={'class': 'form-control'}),
			'Email': forms.EmailInput(attrs={'class':'form-control'}),
        }