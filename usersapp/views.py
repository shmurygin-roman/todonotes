from .models import User
from .serializers import UserModelSerializer, UserModelSerializerV2
from rest_framework import mixins, viewsets
#from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer


class UserCustomViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializerV2
        return UserModelSerializer

    #renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
