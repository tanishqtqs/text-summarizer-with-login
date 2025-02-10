from django.urls import path
from .views import PingView, CreateBlogView

urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
]
