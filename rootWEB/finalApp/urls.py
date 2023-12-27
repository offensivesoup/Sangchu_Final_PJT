from django.urls import path, include
from finalApp import views
from finalApp.views import cosine_similarity_view, detail_view, gongsilmap

urlpatterns = [
    path("<str:region_name>/",views.list),
    path("<str:region_name>/<int:maemul_id>/detail/",views.detail),
    path("<str:region_name>/getData/",views.get_list),
    path("<str:region_name>/<int:maemul_id>/detail/getData/",views.get_detail),
    path('<str:region_name>/<int:maemul_id>/detail/cosine/', cosine_similarity_view , name = 'cosine'),
    path('<str:region_name>/<int:maemul_id>/detail/view/', detail_view, name = "views"),
    path('<str:region_name>/', views.gongsilmap)
]
