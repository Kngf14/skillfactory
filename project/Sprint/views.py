from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django_filters import rest_framework

from .serializers import *
from .models import *


class MountainsViewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer

    def create(self, request, *args, **kwargs):
        serializer = MountainSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Запись создана', 'id': serializer.data['id']})

    def update(self, request, *args, **kwargs):
        Mountain = self.get_object()
        serializer = self.get_serializer(Mountain, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'state': 1, 'message': 'Запись изменена'})
        else:
            return Response({'state': 0, 'message': serializer.error})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer
    permission_classes = [permissions.AllowAny]

class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImagesOfMountains.objects.all().order_by('-data')
    serializer_class = ImageSerializer
    permission_classes = [permissions.AllowAny]

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.AllowAny]