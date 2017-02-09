from django.db import models

import datetime

class Dentist(models.Model):

    name = models.CharField('Nome', max_length=100)
    cro = models.CharField('CRO', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Dentista'
        verbose_name_plural = 'Dentistas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Patient(models.Model):

    name = models.CharField('Nome', max_length=100)
    cpf = models.IntegerField('CPF')
    rg = models.IntegerField('RG')
    phone = models.IntegerField('Telefone')

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['name']

    def __str__(self):
        return self.name


class Consultation(models.Model):

    data = models.DateField(blank=True, null=True)
    name = models.ForeignKey('consulta.Patient', verbose_name='Nome do Paciente')
    dentist = models.ForeignKey('consulta.Dentist', verbose_name='Dentista')
    description = models.TextField('Historico', blank=True)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)


    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consulta'
        ordering = ['dentist']
