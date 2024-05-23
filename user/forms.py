from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'password', 'email'}


class LoginForm(forms.Form):
    username = forms.CharField(label='username: ', max_length=30, required=True)
    password = forms.CharField(label='password: ', widget=forms.PasswordInput(), required=True)

class ProfileForm(forms.ModelForm):


    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email'}