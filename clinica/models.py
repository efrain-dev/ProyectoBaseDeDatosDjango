# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User


class Cita(models.Model):
    no_cita = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    paciente_dpi = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='paciente_dpi')
    medico_licencia_medica = models.ForeignKey('Medico', models.DO_NOTHING, db_column='medico_licencia_medica')

    class Meta:
        managed = False
        db_table = 'cita'


class Clinica(models.Model):
    id_clinica = models.AutoField(primary_key=True)
    no_patente = models.CharField(max_length=40, blank=True, null=True)
    nombre = models.CharField(max_length=60, blank=True, null=True)
    direccion = models.CharField(max_length=40, blank=True, null=True)
    auth_user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinica'


class Diagnostico(models.Model):
    id_diagnostico = models.AutoField(primary_key=True)
    evaluacion_inicial = models.CharField(max_length=80, blank=True, null=True)
    evaluacion_final = models.CharField(max_length=80, blank=True, null=True)
    tratamiento_id_tratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING,
                                                   db_column='tratamiento_id_tratamiento')

    class Meta:
        managed = False
        db_table = 'diagnostico'


class HistorialMedico(models.Model):
    observaciones = models.CharField(max_length=80, blank=True, null=True)
    cita_no_cita = models.ForeignKey(Cita, models.DO_NOTHING, db_column='cita_no_cita')
    diagnostico_id_diagnostico = models.ForeignKey(Diagnostico, models.DO_NOTHING,
                                                   db_column='diagnostico_id_diagnostico')
    id_historial = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'historial_medico'


class Medico(models.Model):
    licencia_medica = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'


class Paciente(models.Model):
    dpi = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=40, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    clinica_id_clinica = models.ForeignKey(Clinica, models.DO_NOTHING, db_column='clinica_id_clinica')

    class Meta:
        managed = False
        db_table = 'paciente'


class TelefonoClinica(models.Model):
    id_telefono_clinica = models.AutoField(primary_key=True)
    no_telefono = models.CharField(max_length=10, blank=True, null=True)
    clinica_id_clinica = models.ForeignKey(Clinica, models.DO_NOTHING, db_column='clinica_id_clinica')

    class Meta:
        managed = False
        db_table = 'telefono_clinica'


class TelefonoPaciente(models.Model):
    id_telefono_paciente = models.AutoField(primary_key=True)
    no_telefono = models.CharField(max_length=10, blank=True, null=True)
    paciente_dpi = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente_dpi')

    class Meta:
        managed = False
        db_table = 'telefono_paciente'


class Tratamiento(models.Model):
    id_tratamiento = models.AutoField(primary_key=True)
    control_medico = models.CharField(max_length=80, blank=True, null=True)
    observaciones = models.CharField(max_length=80, blank=True, null=True)
    reseta = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tratamiento'
