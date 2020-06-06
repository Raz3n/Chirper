from django.urls import path
from .forms import ProfileForm
from .views import profile_detail_view

urlpatterns = [
    path('<str:username>', profile_detail_view),
]