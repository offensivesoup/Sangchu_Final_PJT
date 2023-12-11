from django.urls import path, include
from busanApp import views
from .views import fetch_lease_trend_view, fetch_zipgac_number_view, fetch_population_info_view, fetch_store_density_view

urlpatterns = [
    path("", views.fetch_lease_trend_view, name='busan_lease_trend'),
    path("", views.fetch_zipgac_number_view, name='busan_zipgac_number'),
    path("", views.fetch_population_info_view, name='population_info'),
    path("", views.fetch_store_density_view, name='busan')]