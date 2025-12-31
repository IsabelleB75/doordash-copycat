import httpx

BASE_URL = "http://localhost:8000"

# Tests pour /calculate-fee/
def test_calculate_fee_returns_200():
    response = httpx.post(
        f"{BASE_URL}/calculate-fee/",
        json={"distance_km": 10, "weight_kg": 2}
    )
    assert response.status_code == 200

def test_calculate_fee_returns_correct_structure():
    response = httpx.post(
        f"{BASE_URL}/calculate-fee/",
        json={"distance_km": 10, "weight_kg": 2}
    )
    data = response.json()
    assert "delivery_fee" in data

def test_calculate_fee_correct_calculation():
    # Formule: base_fee(5) + fee_per_km(1.5)*distance + fee_per_kg(0.5)*weight
    # 5 + 1.5*10 + 0.5*2 = 5 + 15 + 1 = 21
    response = httpx.post(
        f"{BASE_URL}/calculate-fee/",
        json={"distance_km": 10, "weight_kg": 2}
    )
    data = response.json()
    assert data["delivery_fee"] == 21.0

def test_calculate_fee_invalid_input_returns_422():
    response = httpx.post(
        f"{BASE_URL}/calculate-fee/",
        json={"invalid_field": "test"}
    )
    assert response.status_code == 422

# Tests pour /estimate-time/
def test_estimate_time_returns_200():
    response = httpx.get(f"{BASE_URL}/estimate-time/5")
    assert response.status_code == 200

def test_estimate_time_returns_correct_structure():
    response = httpx.get(f"{BASE_URL}/estimate-time/5")
    data = response.json()
    assert "estimated_delivery_time_minutes" in data

def test_estimate_time_correct_calculation():
    # Formule: base_time(10) + time_per_km(5)*distance
    # 10 + 5*5 = 35
    response = httpx.get(f"{BASE_URL}/estimate-time/5")
    data = response.json()
    assert data["estimated_delivery_time_minutes"] == 35.0
