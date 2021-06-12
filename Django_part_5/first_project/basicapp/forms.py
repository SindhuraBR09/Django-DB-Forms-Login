from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from basicapp.models import UserProfileInfo

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields=('username','email','password')

class UserProfileInfoForm(ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('profile_pic', 'portfolio_site')
