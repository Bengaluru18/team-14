from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields

from .models import Medi, Patient, Appointment, MediAvailability, Reception, SocialWorker


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class MediResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Medi.objects.all()
        resource_name = "medi"


class PatientResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Patient.objects.all()
        resource_name = "patient"


class AppointmentResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Appointment.objects.all()
        resource_name = "appointment"


class MediAvailabilityResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = MediAvailability.objects.all()
        resource_name = "mediavailability"


class ReceptionResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Reception.objects.all()
        resource_name = "reception"


class SocialWorkerResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = SocialWorker.objects.all()
        resource_name = "socialworker"