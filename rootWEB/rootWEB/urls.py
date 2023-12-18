
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('mainApp.urls')),
    path("busan/", include('busanApp.urls')),
    path("region/", include('regionApp.urls')),
    path("maemul/",include('finalApp.urls'))
]
