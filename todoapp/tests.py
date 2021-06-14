import json

from django.test import TestCase
from django.test.utils import captured_output
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import (APIClient, APIRequestFactory,
                                 APISimpleTestCase, APITestCase,
                                 force_authenticate)
from usersapp.models import User

from .models import Project, ToDo
from .views import ProjectModelViewSet, ToDoModelViewSet


class TestProjectModelViewSet(TestCase):
    def test_get(self):
        factory = APIRequestFactory()
        request = factory.get('/api/project/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        client = APIClient()
        response = client.post('/api/project/', data={'name': 'ProjectName', 'link': 'www.link.com', 'users': [1, ]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_admin(self):
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.post('/api/project/', data={'name': 'ProjectName', 'link': 'www.link.com', 'users': [1, ]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        client.logout()
