from django import forms
from django.forms import ModelForm, Textarea,TextInput

from . models import contact,internship
class contactsForm(ModelForm):
    class Meta:
        model = contact
        fields = ['Name','phone',  'email','message']
        widgets = {
            'Name': TextInput(attrs={'placeholder': 'Name'}),
            'phone': TextInput(attrs={'placeholder': 'Phone'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
            'message': Textarea(attrs={'placeholder': 'Message'}),

        }

class internshipForm(ModelForm):
    class Meta:
        model = internship
        fields = ['Name','phone',  'email','message','CV']
        widgets = {
            'Name': TextInput(attrs={'placeholder': 'Name'}),
            'phone': TextInput(attrs={'placeholder': 'Phone'}),
            'email': TextInput(attrs={'placeholder': 'Email'}),
            'message': Textarea(attrs={'placeholder': 'Message'}),

        }