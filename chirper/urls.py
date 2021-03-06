from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from accounts.views import (
    login_view,
    logout_view,
    register_view
)


from chirps.views import (
    home_view,
    chirps_list_view,
    chirps_detail_view,
)


urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('global/', chirps_list_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('<int:chirp_id>', chirps_detail_view),
    re_path(r'profiles?/', include('profiles.urls')),
    path('api/chirps/', include('chirps.api.urls')),
    re_path(r'api/profiles?/', include('profiles.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
