from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('', signup),
    path('authapp.login/', login_view),
    path('authapp.logout/', logout_view),
    path('main/', TemplateView.as_view(template_name='authentications/main.html'), name='main')

]
