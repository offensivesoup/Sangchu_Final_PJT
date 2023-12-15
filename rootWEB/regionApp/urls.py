from django.urls import path, include
from regionApp import views
from .views import *

urlpatterns = [
    path("", views.index),]