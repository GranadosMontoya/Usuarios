from django.urls import path
from .views import *

app_name = 'user_app'
urlpatterns = [
    path('registrer/',
    UserRegistrerCreateView.as_view(),
    name='user_registrer'),
]
