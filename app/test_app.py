import requests
import json

BASE_URL = "http://localhost:5000"

def test_hello():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Hello, World!" in response.text

def test_create_item_success():
    item_data = {
        "name": "Laptop",
        "description": "A powerful machine",
        "price": 1200.99
    }
    response = requests.post(f"{BASE_URL}/items", json=item_data)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["name"] == "Laptop"
    assert response_json["price"] == 1200.99

def test_create_item_failure():
    # Missing required field 'name'
    item_data = {
        "description": "Missing name",
        "price": 10.5
    }
    response = requests.post(f"{BASE_URL}/items", json=item_data)
    assert response.status_code == 400
    assert "errors" in response.json()

def test_external_api():
    response = requests.get(f"{BASE_URL}/external")
    assert response.status_code in [200, 500]  # Acceptable if external fails temporarily
