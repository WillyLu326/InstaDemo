from django.urls import path
from Insta.views import HelloWorld, PostsView, PostDetailView

urlpatterns = [
    path('',  HelloWorld.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
]
