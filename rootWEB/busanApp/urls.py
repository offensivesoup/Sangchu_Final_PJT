from django.urls import path, include
# from busanApp import views
from . import views
from .views import fetch_lease_trend_view, fetch_zipgac_numbers_view
urlpatterns = [
    path("", views.fetch_lease_trend_view, name='busan_lease_trend'),
    path("", views.fetch_zipgac_numbers_view, name='busan_zipgac_numbers'),
]
