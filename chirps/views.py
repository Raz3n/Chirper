import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Chirp
from .forms import ChirpForm
from .serializers import ChirpSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={}, status=200)

@api_view(['POST']) #http method the client sends == post
# @authentication_classes([SessionAuthentication, MyCustomAuth])
@permission_classes([IsAuthenticated])
def chirp_create_view(request, *args, **kwargs):
    serializer = ChirpSerializer(data = request.POST or None)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status = 201)
    return Response({}, status=400)

@api_view(['GET'])
def chirp_detail_view(request, chirp_id , *args, **kwargs):
    qs = Chirp.objects.filter(id=chirp_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ChirpSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def chirp_delete_view(request, chirp_id , *args, **kwargs):
    qs = Chirp.objects.filter(id=chirp_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "You cannot delete this chirp."}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "Chirp removed."}, status=200)

@api_view(['GET'])
def chirp_list_view(request, *args, **kwargs):
    qs = Chirp.objects.all()
    serializer = ChirpSerializer(qs, many=True)
    return Response(serializer.data)


def chirp_create_view_pure_django(request, *args, **kwargs):
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = ChirpForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        if request.is_ajax():
            return JsonResponse( obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = ChirpForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form": form})


def chirp_list_view_pure_django(request, *args, **kwargs):
    qs = Chirp.objects.all()
    chirps_list = [ x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": chirps_list
    }
    return JsonResponse(data)

def chirp_detail_view_pure_django(request, chirp_id, *args, **kwargs):
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
