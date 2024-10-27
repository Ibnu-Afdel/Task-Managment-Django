from django.contrib import admin
from .models import Task , Category , Comment



class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
class TaskAdmin(admin.ModelAdmin) :
    inlines = [
        CommentInline,
    ]

admin.site.register(Task,TaskAdmin )
admin.site.register(Category)
admin.site.register(Comment)