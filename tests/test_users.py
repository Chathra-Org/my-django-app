import pytest
from django.urls import reverse, resolve
from users.views import add_user, update_user, list_users, get_user

def test_add_user_url():
    assert resolve('/users/').view_func == add_user

def test_update_user_url():
    assert resolve('/users/testuser/').view_func == update_user

def test_list_users_url():
    assert resolve('/users/').view_func == list_users

def test_get_user_url():
    assert resolve('/users/testuser/').view_func == get_user

@pytest.mark.django_db
def test_add_user_success():
    url = reverse('add_user')
    data = {'username': 'testuser', 'email': 'test@example.com'}
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data['message'] == 'User testuser created'
    assert response.data['email'] == 'test@example.com'

@pytest.mark.django_db 
def test_add_user_missing_username():
    url = reverse('add_user')
    data = {'email': 'test@example.com'}
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert response.data['error'] == 'Missing username'

@pytest.mark.django_db
def test_update_user_success():
    url = reverse('update_user', args=['testuser'])
    data = {'email': 'new@example.com'}
    response = client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.data['message'] == 'User testuser updated'
    assert response.data['email'] == 'new@example.com'

@pytest.mark.django_db
def test_update_user_missing_email():
    url = reverse('update_user', args=['testuser'])
    data = {}
    response = client.put(url, data, format='json')
    assert response.status_code == 400
    assert response.data['error'] == 'Missing email'

@pytest.mark.django_db
def test_list_users():
    url = reverse('list_users')
    response = client.get(url)
    assert response.status_code == 200
    assert 'users' in response.data
    assert len(response.data['users']) == 3

@pytest.mark.django_db
def test_get_user():
    url = reverse('get_user', args=['testuser'])
    response = client.get(url)
    assert response.status_code == 200
    assert response.data['username'] == 'testuser'
    assert response.data['email'] == 'testuser@example.com'
