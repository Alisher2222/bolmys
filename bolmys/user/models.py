from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    telephone_number = models.CharField(max_length=200)
    user_avatar = models.ImageField()
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'custom user'
        verbose_name_plural = 'custom users'