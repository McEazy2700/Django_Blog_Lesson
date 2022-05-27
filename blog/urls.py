from django.urls import path
from .views import (
    home,
    about,
    PostListView,
    PostDetailtView,
    PostCreatetView,
    PostUpdatetView,
    PostDeletetView
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailtView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdatetView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeletetView.as_view(), name='post-delete'),
    path('post/new/', PostCreatetView.as_view(), name='post-create'),
    path('about', about, name='blog-about'),
]