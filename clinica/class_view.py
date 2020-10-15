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
    form_class = forms.ClinicaForm
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

# # -------------------Seccion de Grado-------------------
#
# class GradoList(ListView):
#     model = models.Grado
#     template_name = 'grados/index.html'
#
#
# class GradoCreate(LoginRequiredMixin, CreateView):
#     model = models.Grado
#     form_class = forms.GradoForm
#     template_name = 'clinica/formCreateEdit.html'
#     success_url = reverse_lazy('grados.index')
#     login_url = 'login'
#
#     def get_success_url(self):
#         return reverse_lazy('grados.index')
#
#
# class GradoUpdate(LoginRequiredMixin, UpdateView):
#     model = models.Grado
#     form_class = forms.GradoForm
#     template_name = 'clinica/formCreateEdit.html'
#     success_url = reverse_lazy('grados.index')
#     login_url = 'login'
#
#     def get_success_url(self):
#         return reverse_lazy('grados.index')
#
#
# class GradoDelete(LoginRequiredMixin, DeleteView):
#     model = models.Grado
#     template_name = 'clinica/clinica_confirm_delete.html'
#     success_url = reverse_lazy('grados.index')
#     login_url = 'login'
#
# # -------------------Seccion de Secciones-------------------
# class SeccionList(ListView):
#     model = models.Seccion
#     template_name = 'secciones/index.html'
#
#
# class SeccionCreate(LoginRequiredMixin, CreateView):
#     model = models.Seccion
#     form_class = forms.SeccionForm
#     template_name = 'clinica/formCreateEdit.html'
#     success_url = reverse_lazy('secciones.index')
#     login_url = 'login'
#
#     def get_success_url(self):
#         return reverse_lazy('secciones.index')
#
#
# class SeccionUpdate(LoginRequiredMixin, UpdateView):
#     model = models.Seccion
#     form_class = forms.SeccionForm
#     template_name = 'clinica/formCreateEdit.html'
#     success_url = reverse_lazy('secciones.index')
#     login_url = 'login'
#
#     def get_success_url(self):
#         return reverse_lazy('secciones.index')
#
#
# class SeccionDelete(LoginRequiredMixin, DeleteView):
#     model = models.Seccion
#     template_name = 'clinica/clinica_confirm_delete.html'
#     success_url = reverse_lazy('secciones.index')
#     login_url = 'login'
#
#
# # -------------------Seccion de Inscripciones-------------------
# class InscripcionList(ListView):
#     model = models.Inscripciones
#     template_name = 'inscripciones/index.html'
#
#
# class InscripcionCreate(LoginRequiredMixin, CreateView):
#     model = models.Inscripciones
#     form_class = forms.InscripcionForm
#     template_name = 'clinica/formCreateEdit.html'
#     success_url = reverse_lazy('inscripciones.index')
#     login_url = 'login'
#
#     def get_success_url(self):
#         return reverse_lazy('inscripciones.index')
#
#
# class InscripcionUpdate(LoginRequiredMixin, UpdateView):
#     model = models.Inscripciones
#     form_class = forms.InscripcionForm
#     template_name = 'clinica/formCreateEdit.html'
#     success_url = reverse_lazy('inscripciones.index')
#     login_url = 'login'
#
#     def get_success_url(self):
#         return reverse_lazy('inscripciones.index')
#
#
# class InscripcionDelete(LoginRequiredMixin, DeleteView):
#     model = models.Inscripciones
#     template_name = 'clinica/clinica_confirm_delete.html'
#     success_url = reverse_lazy('inscripciones.index')
#     login_url = 'login'
