from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from Mobile.models import Orders
from django.forms import ModelForm


class UserCreaForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class OrederForm(forms.ModelForm):
    product=forms.CharField()
    class Meta:
        model=Orders
        fields=["product","address"]

class BuyOrder(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["status"]
