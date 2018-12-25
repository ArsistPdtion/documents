from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    pass

    class Meta:
        model = User

class LogInForm(forms.ModelForm):
    pass

    class Meta:
        model = User