from django.urls import path, include
from mainApp import views
urlpatterns = [
    path("", views.index),
    path("map/", views.map),
    path("busan/",views.busan),
    path("sign2/",views.sign2),
    path("analysis1/",views.analysis_lease),
    path("analysis2/",views.analysis_zipgac),
    # path("analysis3/",)
]
