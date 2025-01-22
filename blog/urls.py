from django.urls import path
from . import views

urlpatterns = [
    # path('create/', views.create_blog, name='create_blog'),
    # path('list/', views.list_blogs, name='list_blogs'),
    path('ping/', views.ping, name='ping'),
]
