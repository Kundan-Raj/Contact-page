from django import forms
from django.core.exceptions import ValidationError
from .models import Contactdb
#from phone_field import PhoneField

class ContactForm(forms.ModelForm):
    comment= forms.CharField(min_length=20, label='Description',widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}))
    #name = models.CharField(max_length=100)
    #phone = forms.PhoneField(blank=True, help_text='Contact phone number')
    name = forms.CharField(max_length=100, min_length=3)
    #phone = forms.PhoneField(max_length=10)
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if "fred@example.com" not in data:
            raise ValidationError("Please enter valid email address.")
        return data
    
    class Meta:
        model= Contactdb
        fields= ("__all__")




