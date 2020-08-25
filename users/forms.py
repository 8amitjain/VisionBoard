from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import Profile


class UserRegistrationFrom(UserCreationForm):
    # email = forms.EmailField()
    # first_name = forms.CharField(max_length=15)
    # last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
# username',


class UserUpdateForm(forms.ModelForm):
    # email = forms.EmailField()
    # first_name = forms.CharField(max_length=15)
    # last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
# 'username',

