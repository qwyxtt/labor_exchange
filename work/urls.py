from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('index/', index, name='index'),
    path('task/', task_history, name='task'),
    path('create_task/', create_task, name='create_task'),
    path('history_of_task/', task_history_employee, name='history_of_task'),
    path('work/', work, name='work')
]
