from django.urls import path
from Insta.views import HelloWorld

urlpatterns = [
    path('',  HelloWorld.as_view(), name='home')
]
