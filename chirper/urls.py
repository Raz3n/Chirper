from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


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
    path('react/', TemplateView.as_view(template_name='react.html')),
    path('create-chirp', chirp_create_view),
    path('chirps', chirp_list_view),
    path('chirps/<int:chirp_id>', chirp_detail_view),
    path('api/chirps/', include('chirps.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
