from .models import Brand_Field,Mobile_Details
from django import forms


from django.forms import ModelForm

class Brand_Create_Form(forms.ModelForm):
    class Meta:
        model=Brand_Field
        fields="__all__"

class Mobile_Create_Form(forms.ModelForm):
    class Meta:
        model=Mobile_Details
        fields="__all__"

class Mobile_Update_Form(forms.ModelForm):
    class Meta:
        model=Mobile_Details
        fields="__all__"







