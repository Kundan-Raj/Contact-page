from django.db import models
from phone_field import PhoneField


class MyModel(models.Model):
    #name = models.CharField(max_length=100)
    #phone = PhoneField(blank=True, help_text='Contact phone number')
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    phone= models.CharField(max_length=30)
    comment= models.CharField(max_length=100)


