import pytest
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


class TestTocketAuth(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_token_auth(self):
        """
            Test  of user registration and getting token for authorization
        """
        url = reverse('user_registation')
        user = dict(username='test_user_registration', password='f01071998', first_name='Denis', last_name='Testovich')
        response = self.client.post(url, user)
        assert response.status_code != 400
        url = reverse('token_obtain_pair')
        response = self.client.post(url, user)
        assert response.data['access'] is not None
