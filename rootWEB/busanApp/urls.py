from django.urls import path, include
from busanApp import views
urlpatterns = [
    path("busan/", views.index, name='busan'),
]
