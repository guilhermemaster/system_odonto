from django.contrib import admin

# Register your models here.

from .models import Dentist, Patient, Consultation, Recepcionista, Assistente



admin.site.register(Dentist)
admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(Recepcionista)
admin.site.register(Assistente)
