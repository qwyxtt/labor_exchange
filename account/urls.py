from django.urls import path
from .views import *

urlpatterns = [
    path('account/', account_of_empoyer, name='account')
]
