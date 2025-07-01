from django.db import models
from django.utils import timezone
# Create your models here.


class Gender(models.Model):
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    date_of_birth = models.DateField(default=timezone.now)

    def __str__(self):
        return self.first_name
