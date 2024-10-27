from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField( max_length=150)

    def __str__(self):
        return self.name
    


class Task(models.Model):
    title = models.CharField( max_length=150)
    short_body = models.CharField( max_length=255)
    long_body = models.TextField(null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    posted_in = models.DateTimeField( auto_now_add=True)
    updated_in = models.DateTimeField (auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    task = models.ForeignKey( Task , on_delete=models.CASCADE)
    comment = models.CharField( max_length=150)
    commenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self) :
        return reverse('detail')
    
    