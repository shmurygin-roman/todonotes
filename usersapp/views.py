from .models import User
from .serializers import UserModelSerializer
from rest_framework import mixins, viewsets
#from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class UserCustomViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    #renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
