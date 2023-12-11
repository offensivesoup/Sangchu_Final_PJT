from os import path

from . import views
from .views import fetch_lease_trend_view, fetch_zipgac_number_view, fetch_population_info_view, fetch_store_density_view,json_store_density_view
from .views import json_store_density_view,json_lease_trend_view,json_zipgac_number_view,json_population_info_view
urlpatterns = [
    path("", views.fetch_lease_trend_view     , name='busan_lease_trend'),
    path("", views.fetch_zipgac_number_view   , name='busan_zipgac_numbers'),
    path("", views.fetch_population_info_view , name='fetch_population_info_view'),
    path("", views.fetch_store_density_view   , name='busan'),
    path("json1/", json_store_density_view    , name='json_store_density_view'),
    path("json2/", json_lease_trend_view      , name='json_lease_trend_view'),
    path("json3/", json_zipgac_number_view    , name='json_lease_trend_view'),
    path("json4/", json_population_info_view  , name='json_population_info_view')

]