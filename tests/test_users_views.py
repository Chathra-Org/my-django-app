import pytest
from django.test import Client
from django.urls import reverse
import json

def test_add_user_view():
    client = Client()
    response = client.post(reverse('add_user'), data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}), content_type='application/json')
    assert response.status_code == 201
    assert response.json() == {'message': 'User testuser created', 'email': 'test@example.com'}

    # Test missing username
    response = client.post(reverse('add_user'), data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing username'}

    # Test missing username and email
    response = client.post(reverse('add_user'), data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing username or email'}

    # Test invalid JSON
    response = client.post(reverse('add_user'), data='invalid json', content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid JSON'}

def test_list_users_view():
    client = Client()
    response = client.get(reverse('list_users'))
    assert response.status_code == 200
    assert response.json() == {'users': ['user1', 'user2', 'user3']}

    # Test invalid method
    response = client.post(reverse('list_users'))
    assert response.status_code == 405
    assert response.json() == {'error': 'Invalid method'}