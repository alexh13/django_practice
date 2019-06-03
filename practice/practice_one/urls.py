from django.urls import path
from . import views

from django.contrib import admin
from django.urls import path
from .views import Homeview

urlpatterns = [
    path('first/', Homeview.as_view(), name='base')
]
