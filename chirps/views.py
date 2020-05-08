from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Chirp

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def chirp_list_view(request, *args, **kwargs):
    qs = Chirp.objects.all()
    chirps_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": chirps_list
    }
    return JsonResponse(data)

def chirp_detail_view(request, chirp_id, *args, **kwargs):
    data = {
        "id": chirp_id,
    }
    status = 200
    try:
        obj = Chirp.objects.get(id=chirp_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)
