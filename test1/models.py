from django.db import models
from phone_field import PhoneField

class Contactdb(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    #phone= models.CharField(max_length=100, blank = True, null = True)
    phone = PhoneField(null=False, blank=True)
    comment= models.CharField(max_length=500, null = False)
    
    def __str__(self):
        return self.name
    
  
   


