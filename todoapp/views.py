from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer, HTMLFormRenderer, BrowsableAPIRenderer
from .models import *
from .serializers import *


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

