from django.db import models


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    disorder = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)


class Medi(models.Model):
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

    comments = models.CharField(max_length=500)


class Reception(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)


class SocialWorker(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)