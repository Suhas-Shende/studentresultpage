
from django.forms import ModelForm
# from django.forms.models import _Labels
from django.forms.widgets import Widget
from .models import *
from django import forms

class studentform(ModelForm):
    
    class Meta:
        model = Person
        fields = '__all__'

class venueForm(ModelForm):
    class Meta:
        model = Person
        fields = ['reg','name','subject','mark']
        Widgets = {
             'reg' : forms.TextInput(attrs={'class ':' form-control'}),
             'name' : forms.TextInput(attrs={'class ':' form-control'}),
             'subject' : forms.TextInput(attrs={'class ':' form-control'}),
             'mark' : forms.TextInput(attrs={'class ':' form-control'}),

                 }