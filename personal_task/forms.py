from django import forms
from .models import MyTaskModel

class MyTaskForm(forms.ModelForm):
    class Meta :
        model = MyTaskModel
        fields = ['title' , 'body'  , 'priority',]