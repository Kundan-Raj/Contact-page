from django import forms
from phone_field import PhoneField


class ContactForm(forms.Form):
    name= forms.CharField(min_length=3, max_length=100, label="Name")
    email= forms.EmailField(max_length=500, label="Email")
    #phone= forms.PhoneField(min_length=10,label="Phone Number (optional)")
    comment= forms.CharField(min_length=20, label='Description',widget=forms.Textarea(
                        attrs={'placeholder': 'Enter your comment here'}))