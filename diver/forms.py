__author__ = 'abdul'
from django import forms
from .models import Diver


class DiverModelForm(forms.ModelForm):
    username = forms.CharField(label=u"Enter Username", max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(label=u"Confirm Password", max_length=30, widget=forms.PasswordInput)
    firstName = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)

    class Meta:
        model = Diver
        fields = ['age', 'phone', 'size']