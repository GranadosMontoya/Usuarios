from django.urls import path
from .views import *

app_name = 'user_app'
urlpatterns = [
    path('registrer/',
        UserRegistrerCreateView.as_view(),
        name='user_registrer'
    ),
    path('login/',
        Login.as_view(),
        name='login'
    ),
    path('logout/',
        Logout.as_view(),
        name='logout'
    ),
    path('update/',
        UpdatePasswordView.as_view(),
        name='update'
    ),
    path('verification/',
        CodeVerificationView.as_view(),
        name='verification'
    ),
    
]
