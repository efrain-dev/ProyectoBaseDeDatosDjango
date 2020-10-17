import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from clinica import forms, models


def clinica_store(request):
    form = forms.ClinicaForm(request.POST)

    if form.is_valid():
        registro = form.save(commit=False)
        registro.auth_user = request.user
        registro.save()
        form = forms.ClinicaForm()
        return HttpResponseRedirect(reverse('clinica.index'))
    return render(request, "clinica/formCreateEdit.html", {"form": form})
