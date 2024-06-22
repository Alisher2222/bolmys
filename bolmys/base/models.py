from django.db import models
from django.conf import settings

class Trip(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length = 200,default='')
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    transport_type = models.CharField(max_length=100)
    user_created = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class UserTrip(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, default='')

    def __str__(self):
        return f'{self.user.username} - {self.trip.name}'
