import pytest
from django.urls import reverse, resolve
from users.views import add_user, list_users

def test_add_user_url():
    assert reverse('add_user') == '/add-user/'
    assert resolve('/add-user/').view_name == 'add_user'

def test_list_users_url():
    assert reverse('list_users') == '/list-users/'
    assert resolve('/list-users/').view_name == 'list_users'