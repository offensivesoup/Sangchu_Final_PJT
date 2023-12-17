from django.urls import path, include
from regionApp import views
from .views import *

urlpatterns = [
    path("<str:region_name>/", views.index),
    # path("chart1/", zipgac_number_chart, name='zipgac_number_chart')
    path("chart1/", get_region_type_data, name='get_lease_trend_data'),
    path("<str:region_name>/chart_data1/", views.chart_float_pop)


]

