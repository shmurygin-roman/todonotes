from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from usersapp.views import UserCustomViewSet
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
#router.register('user', UserCustomViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Todonotes",
      default_version='1.0',
      description="Documentation to out project",
      contact=openapi.Contact(email="admin@ya.ru"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[AllowAny,],
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth/', include('rest_framework.urls')),
   path('api/', include(router.urls)),
   path('api-token-auth/', views.obtain_auth_token),
   path('api/user/1.0/', include('usersapp.urls', namespace='1.0')),
   path('api/user/2.0/', include('usersapp.urls', namespace='2.0')),   
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
