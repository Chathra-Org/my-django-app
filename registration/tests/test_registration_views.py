import pytest
from django.urls import reverse
from registration.models import Registration

@pytest.mark.django_db
def test_registrations_list_page(client):
    Registration.objects.create(first_name='Jane', last_name='Smith', email='jane@example.com')
    Registration.objects.create(first_name='John', last_name='Doe', email='john@example.com')
    response = client.get(reverse('registrations'))
    assert response.status_code == 200
    assert b"Registered Users" in response.content
    assert b"jane@example.com" in response.content
    assert b"john@example.com" in response.content

@pytest.mark.django_db
def test_registrations_list_page_no_registrations(client):
    response = client.get(reverse('registrations'))
    assert response.status_code == 200
    assert b"Registered Users" in response.content
    assert b"No registrations yet." in response.content

@pytest.mark.django_db
def test_registrations_list_page_order_by_registered_at(client):
    reg1 = Registration.objects.create(first_name='Jane', last_name='Smith', email='jane@example.com')
    reg2 = Registration.objects.create(first_name='John', last_name='Doe', email='john@example.com')
    response = client.get(reverse('registrations'))
    assert response.status_code == 200
    assert list(response.context['registrations']) == [reg2, reg1]