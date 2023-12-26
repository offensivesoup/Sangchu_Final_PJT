from django.urls import path, include
from finalApp import views
from .views import cosine_similarity_view, detail_view

urlpatterns = [
    path("<str:region_name>/",views.list),
    path("<str:region_name>/<int:maemul_id>/detail/",views.detail),
    path("<str:region_name>/getData/",views.get_list),
    path("<str:region_name>/<int:maemul_id>/detail/getData/",views.get_detail),
    path('<str:region_name>/<int:maemul_id>/detail/cosine/', cosine_similarity_view , name = 'cosine'),
<<<<<<< HEAD
    # path('toggle_bookmark/<int:maemul_id>/', views.toggle_bookmark, name='toggle_bookmark'),
    path('<str:region_name>/<int:maemul_id>/detail/view/', detail_view, name = "views")

=======
    path('<str:region_name>/<int:maemul_id>/detail/view/', detail_view, name = "views"),
<<<<<<< HEAD
    path("like_view/",views.like_view, name = "like_view")
>>>>>>> c33e9888dc846fef468856325e6b7e29b59643b5
=======
    path("like_view/<int:maemul_id>/<int:user_id>",views.like_view, name = "like_view"),
    path('<str:region_name>/<int:maemul_id>/detail/like_status/',views.like_status)
>>>>>>> 7a64a53ffa7cb6f7d4f4f77504c0919c88fd147a
]
