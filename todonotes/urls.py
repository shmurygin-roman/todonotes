from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from usersapp.views import UserCustomViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('user', UserCustomViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
   path('api-token-auth/', views.obtain_auth_token),
]
