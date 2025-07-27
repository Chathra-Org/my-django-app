import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_homepage_template_content(client):
    response = client.get(reverse('home'))
    assert b'AWS Community Day 2025' in response.content
    assert b'Register' in response.content
    assert b'Building Smarter Developer Platforms' in response.content
