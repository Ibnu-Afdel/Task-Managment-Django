from django.urls import path
from .views import home , create , update , delete , detail , all_post

urlpatterns = [
    path('update/<int:pk>/', update , name= 'update'),
    path('delete/<int:pk>/' , delete , name='delete') ,
    path('detail/<int:pk>/' , detail , name='detail') ,
    path('create/' , create , name='create'),
    path('all/' , all_post , name='all_post'),
    path('' , home , name='home'),
]
