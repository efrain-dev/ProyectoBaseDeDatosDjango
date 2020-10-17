from django import forms
import datetime

from clinica import models


class CitaForm(forms.ModelForm):
    fecha = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = models.Cita
        fields = "__all__"


class ClinicaForm(forms.ModelForm):

    class Meta:
        model = models.Clinica
        fields = ('nombre','no_patente','direccion',)



class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = models.Diagnostico
        fields = "__all__"


class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = models.HistorialMedico
        fields = "__all__"


class MedicoForm(forms.ModelForm):
    class Meta:
        model = models.Medico
        fields = "__all__"


class PacienteForm(forms.ModelForm):
    class Meta:
        model = models.Paciente
        fields = "__all__"


class TelefonoClinicaForm(forms.ModelForm):
    class Meta:
        model = models.TelefonoClinica
        fields = "__all__"


class TelefonoPacienteForm(forms.ModelForm):
    class Meta:
        model = models.TelefonoPaciente
        fields = "__all__"


class TratamientoForm(forms.ModelForm):
    class Meta:
        model = models.Tratamiento
        fields = "__all__"



