from django import forms
from django.forms import ModelForm
from .models import UserSocial

class UserProfileForm(ModelForm):
    class Meta:
        model = UserSocial
        
