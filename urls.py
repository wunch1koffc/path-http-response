from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/<int:post_id>/', views.posts),
    path('posts/<slug:post_slug>/', views.posts_by_slug),
]
