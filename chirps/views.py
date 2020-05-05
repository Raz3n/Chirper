from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Chirp

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse('<h1>Hello World<h1>')


def chirp_detail_view(request, chirp_id, *args, **kwargs):
    try:
        obj = Chirp.objects.get(id=chirp_id)
    except:
        raise Http404
    data = {
        "id": chirp_id,
        "content": obj.content,
        #"image_path": obj.image.ul
        
    }
    return JsonResponse(data)
