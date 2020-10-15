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
from login import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('users/apps', views.welcome, name='apps'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout),

    path('citas/index/', class_view.CitaList.as_view(), name='cita.index'),
    path('citas/create/', class_view.CitaCreate.as_view(), name='cita.create'),
    path('citas/edit/<int:pk>/', class_view.CitaUpdate.as_view(), name='cita.edit'),
    path('citas/delete/<int:pk>/', class_view.CitaDelete.as_view(), name='cita.delete'),


    path('clinicas/index/', class_view.ClinicaList.as_view(), name='clinica.index'),
    path('clinicas/create/', class_view.ClinicaCreate.as_view(), name='clinica.create'),
    path('clinicas/edit/<int:pk>/', class_view.ClinicaUpdate.as_view(), name='clinica.edit'),
    path('clinicas/delete/<int:pk>/', class_view.ClinicaDelete.as_view(), name='clinica.delete'),

]
