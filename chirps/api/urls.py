from django.urls import path

from .views import (
    chirp_action_view,
    chirp_delete_view,
    chirp_detail_view, 
    chirp_list_view,
    chirp_create_view,
    )

urlpatterns = [
    path('', chirp_list_view),
    path('action/', chirp_action_view),
    path('create/', chirp_create_view),
    path('<int:chirp_id>/', chirp_detail_view),
    path('<int:chirp_id>/delete/', chirp_delete_view),
]