from django.urls import path
from .views import list_tasks, create_task, listaTareas, deleteTask

urlpatterns = [
    path('', list_tasks),
    path('new_task/', create_task, name='create_task'),
    path('lista/', listaTareas),
    path('delete_task/<int:task_id>/', deleteTask, name='delete_task'),
]