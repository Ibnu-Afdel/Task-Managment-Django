from django import forms
from .models import Task , Comment

class TaskForm(forms.ModelForm):
    class Meta :
        model = Task
        fields = ['title','short_body','long_body','category',]
        
class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment
        fields = ['comment',]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.instance.task = kwargs.get('task')