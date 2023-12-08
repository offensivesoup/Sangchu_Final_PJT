from django.urls import path, include
from busanApp import views
from .views import fetch_lease_trend_view, fetch_zipgac_numbers_view, fetch_population_info_view, fetch_store_density_view

urlpatterns = [
    path("", views.fetch_lease_trend_view, name='busan_lease_trend'),
    path("", views.fetch_zipgac_numbers_view, name='busan_zipgac_numbers'),
    path("", views.fetch_population_info_view),
    path("", views.fetch_store_density_view, name='busan')]