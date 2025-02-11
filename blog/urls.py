from django.urls import path
from .views import PingView, CreateBlogView, UserBlogsView

urlpatterns = [
    path('ping/', PingView.as_view(), name='ping'),
    path('create/', CreateBlogView.as_view(), name='create_blog'),
    path('my-blogs/', UserBlogsView.as_view(), name='user_blogs'),
]
