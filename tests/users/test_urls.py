import pytest
from django.urls import reverse, resolve
from users import views

def test_add_user_url():
    assert reverse('add_user') == '/users/'
    assert resolve('/users/').view_func == views.add_user

def test_update_user_url():
    assert reverse('update_user', args=['testuser']) == '/users/testuser/'
    assert resolve('/users/testuser/').view_func == views.update_user

def test_list_users_url():
    assert reverse('list_users') == '/users/'
    assert resolve('/users/').view_func == views.list_users

def test_get_user_url():
    assert reverse('get_user', args=['testuser']) == '/users/testuser/'
    assert resolve('/users/testuser/').view_func == views.get_user

def test_delete_user_url():
    assert reverse('delete_user', args=['testuser']) == '/users/testuser/delete/'
    assert resolve('/users/testuser/delete/').view_func == views.delete_user
