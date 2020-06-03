from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from chirps.views import (
    chirps_list_view,
    chirps_detail_view,
    chirps_profile_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', chirps_list_view),
    path('<int:chirp_id>', chirps_detail_view),
    path('profile/<str:username>', chirps_profile_view),
    path('api/chirps/', include('chirps.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
