from django.contrib import admin
from django.urls import path,include
from .views.login_view import TestView

urlpatterns = [
   

    path('test/',TestView.as_view(), name='test'),
]
