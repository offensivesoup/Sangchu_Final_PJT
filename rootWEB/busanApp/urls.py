from os import path
from django.urls import path, include
from . import views
from .views import json_store_density_view,json_lease_trend_view,json_zipgac_number_view,json_population_density_view, json_service_density_view, json_population_cnt_view, predict_model_view
from .views import cosine_similarity_view, population_density_chart, get_lease_trend_data, lease_trend, service_population_json, service_population
urlpatterns = [
    path("", views.index),
    path("json1/", json_store_density_view    , name='json_store_density_view'),
    path("json2/", json_lease_trend_view      , name='json_lease_trend_view'),
    path("json3/", json_zipgac_number_view    , name='json_lease_trend_view'),
    path("json4/", json_population_density_view  , name='json_population_density_view'),
    path("json5/", json_service_density_view , name='json_service_density_view'),
    path("json6/", json_population_cnt_view, name='json_service_density_view'),
    path('predict/', predict_model_view, name='predict_model_view'),
    path('cosine/<int:index>/', cosine_similarity_view, name = 'cosine'),
    path('json_population_density_view/', json_population_density_view, name='json_population_density_view'),
    path('population_density_chart/', population_density_chart, name='population_density_chart'),
    path('get_lease_trend_data/', get_lease_trend_data, name='get_lease_trend_data'),
    path('lease_trend/', lease_trend, name='lease_trend'),
    path('service_population_json/', service_population_json, name='service_population_json'),
    path('service_population/', service_population, name='service_population'),

]
