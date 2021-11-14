from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


app_name = 'seller'

urlpatterns = [
    path('register', views.registration),
    path('login', views.LoginWithEmailView.as_view(), name='token_obtain_pair'),
    
    # Endpoint for getting a new access token once it expires. Makes use of the refresh token to achieve this 
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]