from django.urls import path, include
from regionApp import views
from .views import *

urlpatterns = [
    path("", views.index),
    path("<str:region_name>/", views.index),
    # path("chart1/", zipgac_number_chart, name='zipgac_number_chart')
]

