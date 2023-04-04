from django.urls import path
from .views import account_of_employer

urlpatterns = [
    path('account/', account_of_employer, name='account')
]
