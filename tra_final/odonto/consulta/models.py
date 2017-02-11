from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.models import User



class Dentist(models.Model):

    name = models.ForeignKey(User, default=0)
    cro = models.CharField('CRO', max_length=100)
    tipo = models.ForeignKey(Group, default=0)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Dentista'
        verbose_name_plural = 'Dentistas'
        ordering = ['name']

    def __str__(self):
        return "%s" % self.name

class Recepcionista(models.Model):

    name = models.ForeignKey(User, default=0)
    tipo = models.ForeignKey(Group, default=0)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Recepcionista'
        verbose_name_plural = 'Recepcionistas'
        ordering = ['name']

    def __str__(self):
        return "%s" % self.name


class Assistente(models.Model):

    name = models.ForeignKey(User, default=0)
    tipo = models.ForeignKey(Group, default=0)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Assistente'
        verbose_name_plural = 'Assistentes'
        ordering = ['name']

    def __str__(self):
        return "%s" % self.name


class Patient(models.Model):

    name = models.CharField('Nome', max_length=100)
    cpf = models.IntegerField('CPF')
    rg = models.IntegerField('RG')
    phone = models.IntegerField('Telefone')
    description = models.TextField('Historico', blank=True)

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


    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)




    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consulta'
        ordering = ['dentist']

    def __str__(self):
        return "%s" % self.data
