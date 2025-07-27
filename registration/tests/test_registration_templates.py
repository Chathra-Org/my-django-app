import pytest
from django.urls import reverse
from registration.models import Registration

@pytest.mark.django_db
def test_register_template_fields(client):
    response = client.get(reverse('register'))
    assert b'First Name' in response.content
    assert b'Last Name' in response.content
    assert b'Email' in response.content
    assert b'csrfmiddlewaretoken' in response.content

@pytest.mark.django_db
def test_success_message(client):
    data = {'first_name': 'Test', 'last_name': 'User', 'email': 'test@example.com'}
    response = client.post(reverse('register'), data)
    assert b'Registration successful' in response.content

@pytest.mark.django_db
def test_registrations_listing_template(client):
    Registration.objects.create(first_name='Jane', last_name='Doe', email='jane@example.com')
    response = client.get(reverse('registrations'))
    assert b'Registered Users' in response.content
    assert b'Jane' in response.content
    assert b'Doe' in response.content
    assert b'jane@example.com' in response.content
