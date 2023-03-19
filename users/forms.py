from django import forms
from django.contrib.auth import authenticate
from .models import CustomUser




class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'password')
