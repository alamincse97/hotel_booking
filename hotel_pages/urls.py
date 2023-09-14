from django.urls import path, include
from . import views

urlpatterns = [
    path('room_details/', views.room_details, name='room_details'),
    path('blog_details/', views.blog_details, name='blog_details'),
]