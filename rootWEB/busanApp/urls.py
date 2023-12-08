from django.urls import path, include
from busanApp import views

urlpatterns = [
    path("", views.fetch_store_density_view, name='busan'),
]
