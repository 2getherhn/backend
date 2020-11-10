from django.forms import ModelForm, Form
from django import forms


class ShelterForm(Form):
    number = forms.CharField(max_length=14)
