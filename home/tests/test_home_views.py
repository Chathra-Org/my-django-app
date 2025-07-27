import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_homepage_status(client):
    response = client.get(reverse('home'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_homepage_template(client):
    response = client.get(reverse('home'))
    assert 'home.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_homepage_content(client):
    response = client.get(reverse('home'))
    assert b'AWS Community Day 2025' in response.content
    assert b'Building Smarter Developer Platforms' in response.content

@pytest.mark.django_db
def test_homepage_register_button(client):
    response = client.get(reverse('home'))
    assert b'Register' in response.content
    assert b'href="/register/"' in response.content
