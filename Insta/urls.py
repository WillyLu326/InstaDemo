from django.urls import path
from Insta.views import HelloWorld, PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',  HelloWorld.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="make_post"),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name="update_post"),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name="delete_post"),
]
