from django import forms
from .models import Message



class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }
    
        error_messages = {
            'required' : "This field is required",
            'invalid' : "This field is invalid",
        }

        labels = {
            'name': '',
            'email': '',
            'message': '',
        }

