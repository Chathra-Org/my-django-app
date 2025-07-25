import pytest
from django.urls import reverse
from django.test import Client

# Test cases for users/urls.py
def test_users_url_patterns():
    assert reverse('add_user') == '/users/'
    assert reverse('update_user', args=['testuser']) == '/users/testuser/'
    assert reverse('list_users') == '/users/'
    assert reverse('get_user', args=['testuser']) == '/users/testuser/'
    assert reverse('delete_user', args=['testuser']) == '/users/testuser/delete/'

# Test cases for users/views.py
@pytest.mark.django_db
def test_add_user_success():
    client = Client()
    response = client.post('/users/', data={'username': 'testuser', 'email': 'test@example.com'}, content_type='application/json')
    assert response.status_code == 201
    assert response.json() == {'message': 'User testuser created', 'email': 'test@example.com'}

@pytest.mark.django_db
def test_add_user_missing_username():
    client = Client()
    response = client.post('/users/', data={'email': 'test@example.com'}, content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing username'}

# Add more test cases for update_user, delete_user, list_users, and get_user
