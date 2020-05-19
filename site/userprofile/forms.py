from .models import Profile
from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'avatar')

