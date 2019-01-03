from django import forms


class SignUpForm(forms.Form):
    username = forms.CharField(label='user name', max_length=256)
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)
    email = forms.EmailField()


class LogInForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)
