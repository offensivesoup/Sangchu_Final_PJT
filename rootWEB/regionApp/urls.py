from django.urls import path, include
from regionApp import views
from .views import *

urlpatterns = [
    path("<str:region_name>/", views.index),
    # path("chart1/", zipgac_number_chart, name='zipgac_number_chart')
    path("<str:region_name>/chart1/", get_region_type_data, name='get_region_type_data'),
    path("<str:region_name>/chart2/", get_information_main_data, name='get_information_main_data'),
    path("<str:region_name>/chart3/", get_time_day_age_people_data, name = 'get_time_day_age_people_data'),
    path("<str:region_name>/chart4/", get_final_moving_data, name = 'get_final_moving_data'),
    path("<str:region_name>/chart5/",get_rent_mean_data, name = 'get_rent_mean_data'),
    path("<str:region_name>/chart6/",get_subway_session_data, name = 'get_subway_session_data'),
    path("<str:region_name>/chart7/",get_eval_score_data, name = 'get_eval_score_data'),
    path("<str:region_name>/school_json/", school_json, name = 'school_json'),
    path("<str:region_name>/subwayloc_json/", subwayloc_json, name='subwayloc_json'),
    path("<str:region_name>/hospital_json/", hospital_json, name='hospital_json'),
    path("<str:region_name>/drug_json/", drug_json, name='drug_json'),
    path("<str:region_name>/get_coordinates_init", get_coordinates_init, name='get_coordinates_init'),
    ]

