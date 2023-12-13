from django.urls import path, include
from mainApp import views
urlpatterns = [
    path("", views.index),
    path("map/", views.map),
    path("signup/",views.signup),
    path("busan/",views.busan),
    path("analysis1/",views.analysis_lease)
    path("sign2/",views.sign2),


]
