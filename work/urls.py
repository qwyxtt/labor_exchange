from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('account/', TemplateView.as_view(template_name='authentications/account.html'), name='account'),
    path('index/', index, name='index')
]
