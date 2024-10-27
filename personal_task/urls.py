from django.urls import path
from .views import dashboard , create_task , update_task , delete_task , detail_task 

urlpatterns = [
    path('detail/<int:pk>/' , detail_task , name='detail_task' ),
    path('delete/<int:pk>/' , delete_task , name='delete_task'),
    path('update/<int:pk>' , update_task , name='update_task'),
    path('create/', create_task , name='create_task'),
    path('' , dashboard , name ='dashboard'),
]
