from django.db import models
from django.contrib.auth.models import User
from .constants import  GENDER_TYPE
# Create your models here.



class UserDetails(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return str(self.user.email)
    