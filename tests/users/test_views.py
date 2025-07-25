import pytest
from django.test import Client
from django.urls import reverse
from users import views
import json

@pytest.mark.django_db
def test_add_user():
    client = Client()
    response = client.post(reverse('add_user'), data=json.dumps({'username': 'testuser', 'email': 'test@example.com'}), content_type='application/json')
    assert response.status_code == 201
    assert response.json() == {'message': 'User testuser created', 'email': 'test@example.com'}

    # Test missing username
    response = client.post(reverse('add_user'), data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing username'}

    # Test missing email
    response = client.post(reverse('add_user'), data=json.dumps({'username': 'testuser'}), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing username or email'}

    # Test invalid JSON
    response = client.post(reverse('add_user'), data='invalid json', content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid JSON'}

@pytest.mark.django_db
def test_update_user():
    client = Client()
    response = client.put(reverse('update_user', args=['testuser']), data=json.dumps({'email': 'new@example.com'}), content_type='application/json')
    assert response.status_code == 200
    assert response.json() == {'message': 'User testuser updated', 'email': 'new@example.com'}

    # Test missing email
    response = client.put(reverse('update_user', args=['testuser']), data=json.dumps({}), content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Missing email'}

    # Test invalid JSON
    response = client.put(reverse('update_user', args=['testuser']), data='invalid json', content_type='application/json')
    assert response.status_code == 400
    assert response.json() == {'error': 'Invalid JSON'}

@pytest.mark.django_db
def test_delete_user():
    client = Client()
    response = client.delete(reverse('delete_user', args=['testuser']))
    assert response.status_code == 200
    assert response.json() == {'message': 'User testuser deleted'}

@pytest.mark.django_db
def test_list_users():
    client = Client()
    response = client.get(reverse('list_users'))
    assert response.status_code == 200
    assert response.json() == {'users': ['user1', 'user2', 'user3']}

@pytest.mark.django_db
def test_get_user():
    client = Client()
    response = client.get(reverse('get_user', args=['testuser']))
    assert response.status_code == 200
    assert response.json() == {'username': 'testuser', 'email': 'testuser@example.com'}