from django.urls import path
from .views import *

app_name = 'home_app'
urlpatterns = [
    path('panel/',
        HomePage.as_view(),
        name='panel'
    ),
    path('mixing/',
        TemplatePrueba.as_view(),
        name='mixing'
    ),
]
