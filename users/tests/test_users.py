import json
from django.test import Client

def test_add_user_with_valid_data():
    client = Client()
    data = {
        "username": "testuser",
        "email": "testuser@example.com"
    }
    response = client.post("/users/", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 201
    assert response.json()["message"] == "User testuser created"
    assert response.json()["email"] == "testuser@example.com"

def test_add_user_with_missing_username():
    client = Client()
    data = {
        "email": "testuser@example.com"
    }
    response = client.post("/users/", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400
    assert response.json()["error"] == "Missing username"

def test_add_user_with_missing_email():
    client = Client()
    data = {
        "username": "testuser"
    }
    response = client.post("/users/", data=json.dumps(data), content_type="application/json")
    assert response.status_code == 400
    assert response.json()["error"] == "Missing username or email"

def test_add_user_with_invalid_json():
    client = Client()
    data = "invalid json"
    response = client.post("/users/", data=data, content_type="application/json")
    assert response.status_code == 400
    assert response.json()["error"] == "Invalid JSON"

def test_update_user_with_valid_data():
    client = Client()
    # Create user first
    create_data = {
        "username": "testuser",
        "email": "testuser@example.com"
    }
    resp_create = client.post("/users/", data=json.dumps(create_data), content_type="application/json")
    assert resp_create.status_code == 201
    # Now update
    update_data = {
        "email": "updated@example.com"
    }
    response = client.put("/users/testuser/", data=json.dumps(update_data), content_type="application/json")
    assert response.status_code == 200
    assert response.json()["message"] == "User testuser updated"
    assert response.json()["email"] == "updated@example.com"

def test_update_user_with_missing_email():
    client = Client()
    # Create user first
    create_data = {
        "username": "testuser",
        "email": "testuser@example.com"
    }
    resp_create = client.post("/users/", data=json.dumps(create_data), content_type="application/json")
    assert resp_create.status_code == 201
    # Now update with missing email
    update_data = {}
    response = client.put("/users/testuser/", data=json.dumps(update_data), content_type="application/json")
    assert response.status_code == 400
    assert response.json()["error"] == "Missing email"

def test_update_user_with_invalid_json():
    client = Client()
    # Create user first
    create_data = {
        "username": "testuser",
        "email": "testuser@example.com"
    }
    resp_create = client.post("/users/", data=json.dumps(create_data), content_type="application/json")
    assert resp_create.status_code == 201
    # Now update with invalid json
    update_data = "invalid json"
    response = client.put("/users/testuser/", data=update_data, content_type="application/json")
    assert response.status_code == 400
    assert response.json()["error"] == "Invalid JSON"