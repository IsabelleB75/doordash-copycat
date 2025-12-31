import httpx

BASE_URL = "http://localhost:8000"

def test_root_endpoint_returns_200():
    response = httpx.get(f"{BASE_URL}/")
    assert response.status_code == 200

def test_root_endpoint_returns_welcome_message():
    response = httpx.get(f"{BASE_URL}/")
    data = response.json()
    assert "message" in data
    assert "Welcome" in data["message"]
