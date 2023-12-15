from django.urls import path, include
from regionApp import views
from .views import *

urlpatterns = [
    path("", views.index),
    path("chart1/", get_region_type_data, name='get_lease_trend_data')]