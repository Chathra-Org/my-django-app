import pytest
from registration.models import Registration

@pytest.mark.django_db
def test_registration_model_save():
    reg = Registration.objects.create(first_name='Test', last_name='User', email='testuser@example.com')
    assert Registration.objects.filter(email='testuser@example.com').exists()

@pytest.mark.django_db
def test_registration_str():
    reg = Registration(first_name='Test', last_name='User', email='testuser@example.com')
    assert str(reg) == 'Test User (testuser@example.com)'

@pytest.mark.django_db
def test_email_uniqueness():
    Registration.objects.create(first_name='A', last_name='B', email='unique@example.com')
    with pytest.raises(Exception):
        Registration.objects.create(first_name='C', last_name='D', email='unique@example.com')
