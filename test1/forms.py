from django import forms
from .models import Contactdb

class ContactForm(forms.ModelForm):
    comment= forms.CharField(label='Description',widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}))
    #name = models.CharField(max_length=100)
    #phone = PhoneField(blank=True, help_text='Contact phone number')
    class Meta:
        model= Contactdb
        fields= ("__all__")




