import httpx

BASE_URL = "http://localhost:8000"

def test_status_endpoint_returns_200():
    response = httpx.get(f"{BASE_URL}/status/")
    assert response.status_code == 200

def test_status_endpoint_returns_running():
    response = httpx.get(f"{BASE_URL}/status/")
    data = response.json()
    assert "status" in data
    assert "running" in data["status"].lower()
