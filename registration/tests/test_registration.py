import pytest
from django.urls import reverse
from registration.models import Registration

@pytest.mark.django_db
def test_registration_page_renders(client):
    response = client.get(reverse('register'))
    assert response.status_code == 200
    assert b"Register" in response.content

@pytest.mark.django_db
def test_successful_registration(client):
    data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'}
    response = client.post(reverse('register'), data)
    assert response.status_code == 302  # Redirect to success page
    assert Registration.objects.filter(email='john@example.com').exists()
    assert b"Registration successful" in response.content

@pytest.mark.django_db
@pytest.mark.parametrize("data", [
    {'last_name': 'Doe', 'email': 'john@example.com'},  # missing first_name
    {'first_name': 'John', 'email': 'john@example.com'},  # missing last_name
    {'first_name': 'John', 'last_name': 'Doe'},  # missing email
])
def test_registration_missing_fields(client, data):
    response = client.post(reverse('register'), data)
    assert response.status_code == 200
    assert b"This field is required." in response.content
    assert Registration.objects.count() == 0

@pytest.mark.django_db
def test_registration_invalid_email(client):
    data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'not-an-email'}
    response = client.post(reverse('register'), data)
    assert response.status_code == 200
    assert b"Enter a valid email address." in response.content
    assert Registration.objects.count() == 0

@pytest.mark.django_db
def test_registration_duplicate_email(client):
    Registration.objects.create(first_name='Jane', last_name='Smith', email='jane@example.com')
    data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'jane@example.com'}
    response = client.post(reverse('register'), data)
    assert response.status_code == 200
    assert b"A user with this email address already exists." in response.content
    assert Registration.objects.count() == 1  # Only the first registration exists

@pytest.mark.django_db
def test_registrations_list_page(client):
    Registration.objects.create(first_name='Jane', last_name='Smith', email='jane@example.com')
    response = client.get(reverse('registrations'))
    assert response.status_code == 200
    assert b"Registered Users" in response.content
    assert b"jane@example.com" in response.content
