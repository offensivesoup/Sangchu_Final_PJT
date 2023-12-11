from django.urls import path, include
from . import views
from .views import json_store_density_view,json_lease_trend_view,json_zipgac_number_view,json_population_density_view, json_service_density_view, json_population_cnt_view
urlpatterns = [
    path("json1/", json_store_density_view    , name='json_store_density_view'),
    path("json2/", json_lease_trend_view      , name='json_lease_trend_view'),
    path("json3/", json_zipgac_number_view    , name='json_lease_trend_view'),
    path("json4/", json_population_density_view  , name='json_population_density_view'),
    path("json5/", json_service_density_view , name='json_service_density_view'),
    path("json6/", json_population_cnt_view, name='json_service_density_view')
]
