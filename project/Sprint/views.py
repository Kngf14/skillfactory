from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django_filters import rest_framework

from .serializers import MountainSerializer
from .models import Mountain


class MountainsViewset(viewsets.ModelViewSet):
    queryset = Mountain.objects.all()
    serializer_class = MountainSerializer

    def create(self, request, *args, **kwargs):
        serializer = MountainSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Запись создана', 'id': serializer.data['id']})

    def partial_update(self, request, *args, **kwargs):
        Mountain = self.get_object()
        serializer = self.get_serializer(Mountain, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'state': 1, 'message': 'Запись изменена'})
        else:
            return Response({'state': 0, 'message': serializer.error})