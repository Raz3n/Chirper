from django.contrib import admin
from django.urls import path

from chirps.views import home_view, chirp_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('chirps/<int:chirp_id>', chirp_detail_view),
]
