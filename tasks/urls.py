from django.urls import path

from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
]
