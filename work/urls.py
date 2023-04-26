from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('index/', index, name='index'),
    path('task/', task_history, name='task'),
    path('create_task/', create_task, name='create_task'),
    path('history_of_task/', task_history_employee, name='history_of_task'),
    path('work/', work, name='work'),
    path('task/<int:task_id>/', accept_task, name='accept_task'),
    path('get_task/', TemplateView.as_view(template_name='work/get_work.html'), name='get_work'),
    path('task/<int:task_id>/go-to-task', go_to_task, name='go_to_task'),
    path('end_task/<int:task_id>/', end_task, name='end_task'),
]
