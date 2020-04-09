from django import forms
from django.forms import ModelForm

from . models import Author
class Subscribe(ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']