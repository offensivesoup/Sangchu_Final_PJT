from django.urls import path, include
from busanApp import views
urlpatterns = [
    path("", views.index),
]
