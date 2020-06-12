import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url


ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/feed.html")

def chirps_list_view(request, *args, **kwargs):
    return render(request, "chirps/list.html")

def chirps_detail_view(request, chirp_id, *args, **kwargs):
    return render(request, "chirps/detail.html", context={"chirp_id": chirp_id} )