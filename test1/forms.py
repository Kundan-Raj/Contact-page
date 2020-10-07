from django import forms
from .models import Contactdb

class ContactForm(forms.ModelForm):
    comment= forms.CharField(label='Description',widget=forms.Textarea(attrs={'placeholder': 'Enter your comment here'}))
    name = forms.CharField(max_length=100, min_length=3)
    
    
    class Meta:
        model= Contactdb
        fields= ("__all__")
        
 # class ContactForm(forms.Form):
    #name= forms.CharField(min_length=3, max_length=100, label="Name")
    #email= forms.EmailField(max_length=500, label="Email")
    #phone= forms.PhoneField(min_length=10,label="Phone Number (optional)")
    #comment= forms.CharField(min_length=20, label='Description',widget=forms.Textarea(
                        #attrs={'placeholder': 'Enter your comment here'}))




