import random

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect

from .models import Chirp
from .forms import ChirpForm

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

def chirp_create_view(request, *args, **kwargs):
    form = ChirpForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form = ChirpForm()
    return render(request, 'components/form.html', context={"form": form})


def chirp_list_view(request, *args, **kwargs):
    qs = Chirp.objects.all()
    chirps_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 999) } for x in qs]
    data = {
        "isUser": False,
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
