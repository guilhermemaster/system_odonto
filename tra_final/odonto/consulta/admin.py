from django.contrib import admin

# Register your models here.

from .models import Dentist, Patient, Consultation

admin.site.register(Dentist)
admin.site.register(Patient)
admin.site.register(Consultation)
