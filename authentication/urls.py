from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view),
    path('main/', TemplateView.as_view(template_name='authentications/main.html'), name='main'),
]
