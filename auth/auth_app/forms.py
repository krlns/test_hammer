from django import forms
from .models import User


class PhoneLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=20)


class AcceptCode(forms.Form):
    code = forms.CharField(max_length=4)


class Profile(forms.Form):
    activate = forms.CharField(max_length=6)
