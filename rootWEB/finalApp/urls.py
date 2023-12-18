from django.urls import path, include
from finalApp import views
urlpatterns = [
    path("",views.list),
    path("detail/<int:maemul_id>",views.detail)

]
