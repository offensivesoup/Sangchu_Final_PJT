from django.urls import path, include
from mainApp import views
urlpatterns = [
    path("", views.index),
    path("map/", views.map),
    path("busan/",views.busan),
    path("sign2/",views.sign2),
    path("analysis1/",views.analysis_lease),
    path("kakaomap/",views.kakaomap),
    path("analysis2/",views.analysis_zipgac),
    path("analysis3/",views.analysis_pop_density),
    path("analysis4/",views.analysis_pop_cnt),
    path("analysis5/",views.analysis_service_cnt),
    path("analysis6/",views.analysis_store_density),
    path('hospital_json/',views.hospital_json),
    path('hospital/',views.hospital),
    path('school_json/',views.school_json),
    path('school/',views.school),
    path('get_center_coordinates/',views.get_center_coordinates),
    path('subwayloc_json/', views.subwayloc_json),
    path('subwayloc/', views.subwayloc),
    path('busstop_json/', views.busstop_json),
    path('busstop/', views.busstop),
]
