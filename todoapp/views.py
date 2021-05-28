from rest_framework.renderers import (BrowsableAPIRenderer, HTMLFormRenderer,
                                      JSONRenderer)
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ToDoLimitOffsetPagination
    filterset_fields = ['project']

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk=None):
        queryset = get_object_or_404(ToDo, pk=pk)
        queryset.is_active = False
        queryset.save()
        serializer_class = ToDoSerializer
        return Response(serializer_class.data)
