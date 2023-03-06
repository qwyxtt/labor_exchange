from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('success/', TemplateView.as_view(template_name='authentications/success.html'), name='success'),
    path('main/', TemplateView.as_view(template_name='work/main.html'), name='main'),
]
