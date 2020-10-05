from django.db import models

class Contactdb(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField()
    phone= models.CharField(max_length=100, blank = True, null = True)
    content= models.CharField(max_length=500, null = False)
    
    def __str__(self):
        return self.name
    
   # class ContactForm(forms.Form):
    #name= forms.CharField(min_length=3, max_length=100, label="Name")
    #email= forms.EmailField(max_length=500, label="Email")
    #phone= forms.PhoneField(min_length=10,label="Phone Number (optional)")
    #comment= forms.CharField(min_length=20, label='Description',widget=forms.Textarea(
                        #attrs={'placeholder': 'Enter your comment here'}))
   


