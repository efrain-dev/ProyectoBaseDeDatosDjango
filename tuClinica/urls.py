"""tuClinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from tuClinica.views import home
from clinica import class_view
from login.views import welcome,login,register,logout
from django.urls import path, include
from clinica.views import clinica_store
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('users/apps', welcome, name='apps'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout),

    path('citas/index/', class_view.CitaList.as_view(), name='cita.index'),
    path('citas/create/', class_view.CitaCreate.as_view(), name='cita.create'),
    path('citas/edit/<str:pk>/', class_view.CitaUpdate.as_view(), name='cita.edit'),
    path('citas/delete/<str:pk>/', class_view.CitaDelete.as_view(), name='cita.delete'),


    path('clinicas/index/', class_view.ClinicaList.as_view(), name='clinica.index'),
    path('clinicas/create/', clinica_store, name='clinica.create'),
    path('clinicas/edit/<int:pk>/', class_view.ClinicaUpdate.as_view(), name='clinica.edit'),
    path('clinicas/delete/<int:pk>/', class_view.ClinicaDelete.as_view(), name='clinica.delete'),

    path('pacientes/index/', class_view.PacienteList.as_view(), name='paciente.index'),
    path('pacientes/create/', class_view.PacienteCreate.as_view(), name='paciente.create'),
    path('pacientes/edit/<int:pk>/', class_view.PacienteUpdate.as_view(), name='paciente.edit'),
    path('pacientes/delete/<int:pk>/', class_view.PacienteDelete.as_view(), name='paciente.delete'),

    path('medicos/index/', class_view.MedicoList.as_view(), name='medico.index'),
    path('medicos/create/', class_view.MedicoCreate.as_view(), name='medico.create'),
    path('medicos/edit/<str:pk>/', class_view.MedicoUpdate.as_view(), name='medico.edit'),
    path('medicos/delete/<str:pk>/', class_view.MedicoDelete.as_view(), name='medico.delete'),

    path('historial-medicos/index/', class_view.HistorialMedicoList.as_view(), name='historial-medico.index'),
    path('historial-medicos/create/', class_view.HistorialMedicoCreate.as_view(), name='historial-medico.create'),
    path('historial-medicos/edit/<str:pk>/', class_view.HistorialMedicoUpdate.as_view(), name='historial-medico.edit'),
    path('historial-medicos/delete/<str:pk>/', class_view.HistorialMedicoDelete.as_view(), name='historial-medico.delete'),

    path('diagnosticos/index/', class_view.DiagnosticoList.as_view(), name='diagnostico.index'),
    path('diagnosticos/create/', class_view.DiagnosticoCreate.as_view(), name='diagnostico.create'),
    path('diagnosticos/edit/<str:pk>/', class_view.DiagnosticoUpdate.as_view(), name='diagnostico.edit'),
    path('diagnosticos/delete/<str:pk>/', class_view.DiagnosticoDelete.as_view(),name='diagnostico.delete'),

    path('tratamientos/index/', class_view.TratamientoList.as_view(), name='tratamiento.index'),
    path('tratamientos/create/', class_view.TratamientoCreate.as_view(), name='tratamiento.create'),
    path('tratamientos/edit/<str:pk>/', class_view.TratamientoUpdate.as_view(), name='tratamiento.edit'),
    path('tratamientos/delete/<str:pk>/', class_view.TratamientoDelete.as_view(), name='tratamiento.delete'),
]
