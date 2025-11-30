# defines django forms for login and creating an admin user
# helps validate input and render forms in templates

from django import forms
from django.contrib.auth.models import User

class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="username")
    password = forms.CharField(widget=forms.PasswordInput, label="password")

class CreateAdminForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="password")

    class Meta:
        model = User
        fields = ['username', 'password']
