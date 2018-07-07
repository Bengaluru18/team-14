from tastypie.resources import ModelResource
from .models import Medi, Patient, Appointment, MediAvailability, Reception, SocialWorker


class MediResource(ModelResource):
    class Meta:
        queryset = Medi.objects.all()
