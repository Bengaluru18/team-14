from tastypie.resources import ModelResource
from .models import Medi, Patient, Appointment, MediAvailability, Reception, SocialWorker


class MediResource(ModelResource):
    class Meta:
        queryset = Medi.objects.all()
        resource_name = "medi"


class PatientResource(ModelResource):
    class Meta:
        queryset = Patient.objects.all()
        resource_name = "patient"


class AppointmentResource(ModelResource):
    class Meta:
        queryset = Appointment.objects.all()
        resource_name = "appointment"


class MediAvailabilityResource(ModelResource):
    class Meta:
        queryset = MediAvailability.objects.all()


class ReceptionResource(ModelResource):
    class Meta:
        queryset = Reception.objects.all()


class SocialWorkerResource(ModelResource):
    class Meta:
        queryset = SocialWorker.objects.all()
