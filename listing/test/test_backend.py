"""Test cases for backend"""
from django.http import HttpRequest
from django.test import TestCase
from django.contrib.auth import get_user_model
from listing.backends import CustomLogin


class BackendTest(TestCase):
    """Custom Login Backend test case"""

    def setUp(self):
        self.backend = CustomLogin()

        self.credentials = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'secret',
            'is_active': True
        }
        get_user_model().objects.create_user(**self.credentials)

    def test_custom_backend_success(self):
        """Test success login with custom backend"""
        user = self.backend.authenticate(
            HttpRequest(),
            username=self.credentials.get('email'),
            password=self.credentials.get('password'))

        assert user.email == self.credentials.get('email')
        assert user.username == self.credentials.get('username')

    def test_custom_backend_failure(self):
        """Test failed login with custom backend"""
        user = self.backend.authenticate(
            HttpRequest(),
            username='test@abc.com',
            password=self.credentials.get('password'))

        assert user is None


