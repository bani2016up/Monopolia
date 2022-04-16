
from email.policy import default
from django import forms
from .models import *

class addForm(forms.Form):
    summa = forms.IntegerField()
    pin = forms.IntegerField()