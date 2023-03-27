from django.urls import path
from .views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('acc/', TemplateView.as_view(template_name='account/employer.html'), name='employer'),
    path('exit/', TemplateView.as_view(template_name='account/exit.html'), name='exit')

]