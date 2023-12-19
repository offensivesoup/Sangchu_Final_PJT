from django.urls import path, include
from finalApp import views
urlpatterns = [
    path("<str:region_name>/",views.list),
    path("detail/",views.detail),
    path("<str:region_name>/getData/",views.get_list)
]
