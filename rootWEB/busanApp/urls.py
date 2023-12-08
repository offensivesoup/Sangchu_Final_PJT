from django.urls import path, include
from busanApp import views
from . import views
from .views import fetch_population_info_view

urlpatterns = [
    path("", views.fetch_population_info_view),
]
