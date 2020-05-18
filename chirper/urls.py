from django.contrib import admin
from django.urls import path

from chirps.views import (
    home_view,
    chirp_action_view,
    chirp_delete_view,
    chirp_detail_view, 
    chirp_list_view,
    chirp_create_view,)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create-chirp', chirp_create_view),
    path('chirps', chirp_list_view),
    path('chirps/<int:chirp_id>', chirp_detail_view),
    path('api/chirps/action', chirp_action_view),
    path('api/chirps/<int:chirp_id>/delete', chirp_delete_view),
]
