from django.contrib import admin
from .models import Patient, Medi, MediAvailability, Appointment, Reception, SocialWorker


# Register your models here.
admin.site.register(Patient)
admin.site.register(Medi)
admin.site.register(MediAvailability)
admin.site.register(Appointment)
admin.site.register(Reception)
admin.site.register(SocialWorker)