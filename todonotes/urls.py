from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usersapp.views import UserModelViewSet
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
]
