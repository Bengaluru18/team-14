from tastypie.resources import ModelResource
from django.contrib.auth.models import User
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from .models import Medi, Patient, Appointment, MediAvailability, Reception, SocialWorker


class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        authorization = Authorization()
        resource_name = 'user'


class MediResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Medi.objects.all()
        authorization = Authorization()
        resource_name = "medi"
        filtering = {
            "id": ALL,
            "user": ALL_WITH_RELATIONS,
            "name": ALL,
            "phone": ALL,
            "spec": ALL,
        }


class PatientResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Patient.objects.all()
        authorization = Authorization()
        resource_name = "patient"
        filtering = {
            "id": ALL,
            "user": ALL_WITH_RELATIONS,
            "name": ALL,
            "age": ALL,
            "phone": ALL,
            "address": ALL,
        }


class AppointmentResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')
    medi = fields.ForeignKey(MediResource, 'medi')
    patient = fields.ForeignKey(PatientResource, 'patient')

    class Meta:
        queryset = Appointment.objects.all()
        authorization = Authorization()
        resource_name = "appointment"
        filtering = {
            "id": ALL,
            "medi": ALL_WITH_RELATIONS,
            "patient": ALL_WITH_RELATIONS,
            "start_time": ['gte', 'lte'],
            "end_time": ['gte', 'lte'],
            "cancelled": ALL,
            "confirmed": ALL,
        }


class MediAvailabilityResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')
    medi = fields.ForeignKey(MediResource, 'medi')

    class Meta:
        queryset = MediAvailability.objects.all()
        authorization = Authorization()
        resource_name = "mediavailability"
        filtering = {
            "id": ALL,
            "medi": ALL_WITH_RELATIONS,
            "start_time": ['gte', 'lte'],
            "end_time": ['gte', 'lte'],
        }


class ReceptionResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Reception.objects.all()
        authorization = Authorization()
        resource_name = "reception"
        filtering = {
            "user": ALL_WITH_RELATIONS,
            "name": ALL,
            "phone": ALL,
            "id": ALL,
        }


class SocialWorkerResource(ModelResource):
    # user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = SocialWorker.objects.all()
        authorization = Authorization()
        resource_name = "socialworker"
        filtering = {
            "user": ALL_WITH_RELATIONS,
            "name": ALL,
            "phone": ALL,
            "id": ALL,
        }