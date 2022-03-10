from pyexpat import model
from attr import fields
from django.core import validators
from django import forms
from matplotlib import widgets
from .models import Ipl

class CreatingTeam(forms.ModelForm):
    class Meta:
        model = Ipl
        fields = ['name', 'team', 'price', 'play', 'role']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'team':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'play':forms.TextInput(attrs={'class':'form-control'}),
            'role':forms.TextInput(attrs={'class':'form-control'}),
            
        }