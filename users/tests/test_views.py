# users/tests/test_views.py
import json
from django.test import Client, TestCase
from django.urls import reverse

class TestDeleteUser(TestCase):
    def test_delete_user_success(self):
        """
        Test that a user can be successfully deleted.
        """
        client = Client()
        response = client.delete(reverse('delete_user', args=['testuser']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'message': 'User testuser deleted'})

    def test_delete_user_invalid_method(self):
        """
        Test that an error is returned for an invalid HTTP method.
        """
        client = Client()
        response = client.get(reverse('delete_user', args=['testuser']))
        self.assertEqual(response.status_code, 405)
        self.assertEqual(json.loads(response.content), {'error': 'Invalid method'})
