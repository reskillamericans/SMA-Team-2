from django import forms
from django.forms import ModelForm
from django.forms.models import fields_for_model
from .models import UserSocial

class UserProfileForm(ModelForm):
    class Meta:
        model = UserSocial
        fields=['facebook','instagram','twitter','linkedin','github']
        
