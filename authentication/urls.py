from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup),
    path('login_view', login_view),
    path('logout/', logout_view)

]