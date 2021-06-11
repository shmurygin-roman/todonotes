import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
#from mixer.backend.django import mixer
from usersapp.models import User
from .views import ProjectModelViewSet, ToDoModelViewSet
from .models import Project, ToDo


class TestProjectModelViewSet(TestCase):
    def test_get(self):
        factory = APIRequestFactory()
        request = factory.get('/api/project/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post(self):
        factory = APIRequestFactory()
        request = factory.post('/api/project/', {'name': 'ProjectName', 'link': 'www.link.com'}, format='json')
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_post_admin(self):
        client = APIClient()
        admin = User.objects.create_superuser('admin1', 'admin@admin.com', 'admin123456')
        client.login(username='admin1', password='admin123456')
        response = client.post('/api/project/', {'name': 'ProjectName', 'link': 'www.link.com'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
