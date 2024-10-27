from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = CustomUser 
        fields = UserCreationForm.Meta.fields + ("userid","age",) 

class CustomuUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields 
