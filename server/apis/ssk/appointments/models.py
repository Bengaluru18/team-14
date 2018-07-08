from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User


# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='patient')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500, blank=True, default=None, null=True)
    disorder = models.CharField(max_length=500, blank=True, default=None, null=True)
    comment = models.CharField(max_length=500,  blank=True, default=None, null=True)


class Medi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='medi')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    spec = models.CharField(max_length=500)


class MediAvailability(models.Model):
    medi = models.ForeignKey(Medi, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Appointment(models.Model):
    medi = models.ForeignKey(Medi, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    confirmed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)

    comments = models.CharField(max_length=500, blank=True, default=None, null=True)


class Reception(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='reception')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)


class SocialWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='socialworker')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)