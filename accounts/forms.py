from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' # allowing all properties to be the feilds of the form

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']