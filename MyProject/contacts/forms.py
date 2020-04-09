from django import forms
from django.forms import ModelForm

from . models import contact,internship
class contactsForm(ModelForm):
    class Meta:
        model = contact
        fields = ['Name','phone',  'email','message']

class internshipForm(ModelForm):
    class Meta:
        model = internship
        fields = ['Name','phone',  'email','message','CV']