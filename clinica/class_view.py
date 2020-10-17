from django.http import HttpRequest
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from clinica import forms, models
from django.contrib.auth.mixins import LoginRequiredMixin


class CitaList(ListView):
    model = models.Cita
    template_name = 'citas/index.html'
    login_url = 'login'


class CitaCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.Cita
    form_class = forms.CitaForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('cita.index')

    def get_success_url(self):
        return reverse_lazy('cita.index')


class CitaUpdate(LoginRequiredMixin, UpdateView):
    model = models.Cita
    form_class = forms.CitaForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('cita.index')
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('cita.index')



class CitaDelete(LoginRequiredMixin, DeleteView):
    model = models.Cita
    template_name = 'clinica/clinica_confirm_delete.html'
    success_url = reverse_lazy('cita.index')
    login_url = 'login'


# # -------------------Clinica-------------------

class ClinicaList(ListView):
    model = models.Clinica
    template_name = 'clinica/index.html'
    login_url = 'login'


class ClinicaCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.Clinica
    form_class = forms.ClinicaForm()
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('clinica.index')

    def get_success_url(self):
        return reverse_lazy('clinica.index')


class ClinicaUpdate(LoginRequiredMixin, UpdateView):
    model = models.Clinica
    form_class = forms.ClinicaForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('clinica.index')
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('clinica.index')


class ClinicaDelete(LoginRequiredMixin, DeleteView):
    model = models.Clinica
    template_name = 'clinica/clinica_confirm_delete.html'
    success_url = reverse_lazy('clinica.index')
    login_url = 'login'

# # -------------------Paciente-------------------

class PacienteList(ListView):
    model = models.Paciente
    template_name = 'paciente/index.html'
    login_url = 'login'


class PacienteCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.Paciente
    form_class = forms.PacienteForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('paciente.index')

    def get_success_url(self):
        return reverse_lazy('paciente.index')


class PacienteUpdate(LoginRequiredMixin, UpdateView):
    model = models.Paciente
    form_class = forms.PacienteForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('paciente.index')
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('paciente.index')


class PacienteDelete(LoginRequiredMixin, DeleteView):
    model = models.Paciente
    template_name = 'clinica/clinica_confirm_delete.html'
    success_url = reverse_lazy('paciente.index')
    login_url = 'login'


# # -------------------Medico-------------------

class MedicoList(ListView):
    model = models.Medico
    template_name = 'medico/index.html'
    login_url = 'login'


class MedicoCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.Medico
    form_class = forms.MedicoForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('medico.index')

    def get_success_url(self):
        return reverse_lazy('medico.index')


class MedicoUpdate(LoginRequiredMixin, UpdateView):
    model = models.Medico
    form_class = forms.MedicoForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('medico.index')
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('medico.index')


class MedicoDelete(LoginRequiredMixin, DeleteView):
    model = models.Medico
    template_name = 'clinica/clinica_confirm_delete.html'
    success_url = reverse_lazy('medico.index')
    login_url = 'login'


# # -------------------Historial-------------------

class HistorialMedicoList(ListView):
    model = models.HistorialMedico
    template_name = 'historial_medico/index.html'
    login_url = 'login'


class HistorialMedicoCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.HistorialMedico
    form_class = forms.HistorialMedicoForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('historial-medico.index')

    def get_success_url(self):
        return reverse_lazy('historial-medico.index')


class HistorialMedicoUpdate(LoginRequiredMixin, UpdateView):
    model = models.HistorialMedico
    form_class = forms.HistorialMedicoForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('historial-medico.index')
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('historial-medico.index')


class HistorialMedicoDelete(LoginRequiredMixin, DeleteView):
    model = models.HistorialMedico
    template_name = 'clinica/clinica_confirm_delete.html'
    success_url = reverse_lazy('historial-medico.index')
    login_url = 'login'


# # -------------------Diagnostico-------------------

class DiagnosticoList(ListView):
    model = models.Diagnostico
    template_name = 'diagnostico/index.html'
    login_url = 'login'


class DiagnosticoCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.Diagnostico
    form_class = forms.DiagnosticoForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('diagnostico.index')

    def get_success_url(self):
        return reverse_lazy('diagnostico.index')


class DiagnosticoUpdate(LoginRequiredMixin, UpdateView):
    model = models.Diagnostico
    form_class = forms.DiagnosticoForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('diagnostico.index')
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('diagnostico.index')


class DiagnosticoDelete(LoginRequiredMixin, DeleteView):
    model = models.Diagnostico
    template_name = 'clinica/clinica_confirm_delete.html'
    success_url = reverse_lazy('diagnostico.index')
    login_url = 'login'


# # -------------------Tratamiento-------------------

class TratamientoList(ListView):
    model = models.Tratamiento
    template_name = 'tratamiento/index.html'
    login_url = 'login'


class TratamientoCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = models.Tratamiento
    form_class = forms.TratamientoForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('tratamiento.index')

    def get_success_url(self):
        return reverse_lazy('tratamiento.index')


class TratamientoUpdate(LoginRequiredMixin, UpdateView):
    model = models.Tratamiento
    form_class = forms.TratamientoForm
    template_name = 'clinica/formCreateEdit.html'
    success_url = reverse_lazy('tratamiento.index')
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('tratamiento.index')


class TratamientoDelete(LoginRequiredMixin, DeleteView):
    model = models.Tratamiento
    template_name = 'clinica/clinica_confirm_delete.html'
    success_url = reverse_lazy('tratamiento.index')
    login_url = 'login'
