from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, PingView

# railway_endpoint = 'text-summarizer-with-login-production.up.railway.app'

urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
