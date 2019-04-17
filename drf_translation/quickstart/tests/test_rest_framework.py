import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
from django.contrib.auth import get_user_model

@pytest.mark.skip
class TestGetAccessToken(APITestCase):
  @pytest.mark.django_db
  def test_get_access_token(self):
    get_user_model().objects.create_superuser('admin_user', 'password')

    self.valid_payload = {
      'username': 'admin_user',
      'password': 'password',
    }

    url = reverse('token_obtain_pair')
    response = self.client.post(url,
                                data=json.dumps(self.valid_payload),
                                content_type='application/json')

    assert response.status_code == status.HTTP_200_OK
