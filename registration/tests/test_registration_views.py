import pytest
from django.urls import reverse
from registration.models import Registration

@pytest.mark.django_db
def test_registration_form_get(client):
    response = client.get(reverse('register'))
    assert response.status_code == 200
    assert 'register.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_registration_post_valid(client):
    data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'}
    response = client.post(reverse('register'), data)
    assert response.status_code == 200
    assert Registration.objects.filter(email='john@example.com').exists()
    assert b'Registration successful' in response.content

@pytest.mark.django_db
def test_registration_post_invalid(client):
    data = {'first_name': '', 'last_name': '', 'email': ''}
    response = client.post(reverse('register'), data)
    assert response.status_code == 200
    assert Registration.objects.count() == 0

@pytest.mark.django_db
def test_registration_duplicate_email(client):
    Registration.objects.create(first_name='Jane', last_name='Doe', email='jane@example.com')
    data = {'first_name': 'Jane', 'last_name': 'Doe', 'email': 'jane@example.com'}
    response = client.post(reverse('register'), data)
    assert Registration.objects.filter(email='jane@example.com').count() == 1

@pytest.mark.django_db
def test_registrations_listing(client):
    Registration.objects.create(first_name='A', last_name='B', email='a@b.com')
    response = client.get(reverse('registrations'))
    assert response.status_code == 200
    assert b'A' in response.content
    assert b'B' in response.content
    assert b'a@b.com' in response.content
