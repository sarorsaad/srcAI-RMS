from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    birth_date = models.DateField()
    

    def __str__(self):
        return self.name
