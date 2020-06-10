import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..models import Chirp
from ..forms import ChirpForm
from ..serializers import (
    ChirpSerializer,
    ChirpActionSerializer,
    ChirpCreateSerializer,
    )

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

@api_view(['POST']) #http method the client sends == post
# @authentication_classes([SessionAuthentication, MyCustomAuth])
@permission_classes([IsAuthenticated])
def chirp_create_view(request, *args, **kwargs):
    serializer = ChirpCreateSerializer(data = request.data)
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chirp_action_view(request, *args, **kwargs):
    '''
        id is required.
        Action options: Like, Unlike, Re-Chirp
    '''
    serializer = ChirpActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        chirp_id = data.get("id")
        action = data.get("action")
        content = data.get("content")
        qs = Chirp.objects.filter(id=chirp_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = ChirpSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = ChirpSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "rechirp":
            new_chirp = Chirp.objects.create(
                    user=request.user,
                    parent=obj,
                    content=content,
                    )
            serializer = ChirpSerializer(new_chirp)
            return Response(serializer.data, status=201)
    return Response({}, status=200)

def get_paginated_queryset_response(qs, request):
    paginator = PageNumberPagination()
    paginator.page_size = 20
    paginated_qs = paginator.paginate_queryset(qs, request)
    serializer = ChirpSerializer(paginated_qs, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def chirp_feed_view(request, *args, **kwargs):
    user = request.user
    qs = Chirp.objects.feed(user)
    return get_paginated_queryset_response(qs, request)

@api_view(['GET'])
def chirp_list_view(request, *args, **kwargs):
    qs = Chirp.objects.all()
    username = request.GET.get('username')
    if username != None:
        qs = qs.by_username(username)
    return get_paginated_queryset_response(qs, request)