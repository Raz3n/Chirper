from django.contrib import admin
from django.urls import path

from chirper.chirps.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
]
