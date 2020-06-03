from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from chirps.views import (
    local_chirps_list_view,
    local_chirps_detail_view,
    local_chirps_profile_view,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', local_chirps_list_view),
    path('<int:chirp_id>', local_chirps_detail_view),
    path('profile/<str:username>', local_chirps_profile_view),
    path('api/chirps/', include('chirps.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
