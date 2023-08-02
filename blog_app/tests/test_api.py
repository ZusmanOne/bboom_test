from rest_framework.test import APIClient
from blog_app.models import Post, User
from django.urls import reverse
import pytest


@pytest.mark.django_db
class TestAuthenticatedEndpoint:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='test text', body='test body', user=self.user)

    def test_authorization_enpoint(self):
        url = reverse('rest_framework:login')
        headers = {'Username': 'testuser',
                   'Password': 'testpassword'}
        response = self.client.get(url, headers=headers)
        assert response.status_code == 200

    def test_authenticated_post_list_endpoint(self):
        url = reverse('post-list')
        self.client.force_authenticate(user=self.user)
        headers = {'Username': 'testuser',
                   'Password': 'testpassword'}
        response = self.client.get(url, headers=headers)

        assert response.status_code == 200

    def test_authenticated_user_list_endpoint(self):
        url = reverse('user-list')
        self.client.force_authenticate(user=self.user)
        headers = {'Username': 'testuser',
                   'Password': 'testpassword'}
        response = self.client.get(url, headers=headers)

        assert response.status_code == 200

    def test_authenticated_user_posts_endpoint(self):
        url = reverse('user_posts', kwargs={'username': self.user.username})
        self.client.force_authenticate(user=self.user)
        headers = {'Username': 'testuser',
                   'Password': 'testpassword'
                   }
        response = self.client.get(url, headers=headers)

        assert response.status_code == 200

    def test_create_post_endpoint(self):
        payload = {
            "title": "test",
            "body": "Test test ",
        }
        self.client.force_authenticate(user=self.user)
        url = reverse('post-list')
        response = self.client.post(url, data=payload, format="json")
        assert response.status_code == 201

    def test_destroy_post(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        assert response.status_code == 204




