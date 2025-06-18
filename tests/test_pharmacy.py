import pytest
from httpx import AsyncClient
from app.models.pharmacy import Medication, Prescription, PharmacyOrder
from app.models.user import User
from app.api.dependencies.auth import get_current_active_user


# Fixtures for test data
@pytest.fixture
def test_medication_data():
    return {
        "name": "Amoxicillin",
        "generic_name": "Amoxicillin",
        "manufacturer": "PharmaCorp",
        "dosage_form": "capsule",
        "strength": "500mg",
        "description": "Antibiotic medication"
    }


@pytest.fixture
def test_prescription_data():
    return {
        "patient_id": 1,
        "doctor_id": 1,
        "medication_id": 1,
        "prescription_date": "2023-01-01",
        "dosage": "1 capsule",
        "frequency": "twice daily",
        "duration": "7 days",
        "instructions": "Take with food",
        "status": "active"
    }


@pytest.fixture
def test_pharmacy_order_data():
    return {
        "prescription_id": 1,
        "pharmacy_id": 1,
        "order_date": "2023-01-01",
        "status": "pending",
        "quantity": 14,
        "notes": "Regular prescription"
    }


# Override get_current_active_user for testing
async def override_get_current_active_user():
    return User(id=1, email="test@example.com", username="testuser", is_active=True)


# Medication Tests
@pytest.mark.asyncio
async def test_create_medication(test_client: AsyncClient, test_medication_data):
    response = await test_client.post("/pharmacy/medications/", json=test_medication_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_medication_data["name"]


@pytest.mark.asyncio
async def test_list_medications(test_client: AsyncClient):
    response = await test_client.get("/pharmacy/medications/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_medication(test_client: AsyncClient):
    # Assuming a medication with ID 1 exists
    response = await test_client.get("/pharmacy/medications/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_medication(test_client: AsyncClient, test_medication_data):
    # Assuming a medication with ID 1 exists
    response = await test_client.put("/pharmacy/medications/1", json=test_medication_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_medication_data["name"]


@pytest.mark.asyncio
async def test_delete_medication(test_client: AsyncClient):
    # Assuming a medication with ID 1 exists
    response = await test_client.delete("/pharmacy/medications/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Prescription Tests
@pytest.mark.asyncio
async def test_create_prescription(test_client: AsyncClient, test_prescription_data):
    response = await test_client.post("/pharmacy/prescriptions/", json=test_prescription_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_prescription_data["patient_id"]


@pytest.mark.asyncio
async def test_list_prescriptions(test_client: AsyncClient):
    response = await test_client.get("/pharmacy/prescriptions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_prescription(test_client: AsyncClient):
    # Assuming a prescription with ID 1 exists
    response = await test_client.get("/pharmacy/prescriptions/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_prescription(test_client: AsyncClient, test_prescription_data):
    # Assuming a prescription with ID 1 exists
    response = await test_client.put("/pharmacy/prescriptions/1", json=test_prescription_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_prescription_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_prescription(test_client: AsyncClient):
    # Assuming a prescription with ID 1 exists
    response = await test_client.delete("/pharmacy/prescriptions/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Pharmacy Order Tests
@pytest.mark.asyncio
async def test_create_pharmacy_order(test_client: AsyncClient, test_pharmacy_order_data):
    response = await test_client.post("/pharmacy/orders/", json=test_pharmacy_order_data)
    assert response.status_code == 200
    data = response.json()
    assert data["prescription_id"] == test_pharmacy_order_data["prescription_id"]


@pytest.mark.asyncio
async def test_list_pharmacy_orders(test_client: AsyncClient):
    response = await test_client.get("/pharmacy/orders/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_pharmacy_order(test_client: AsyncClient):
    # Assuming an order with ID 1 exists
    response = await test_client.get("/pharmacy/orders/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_pharmacy_order(test_client: AsyncClient, test_pharmacy_order_data):
    # Assuming an order with ID 1 exists
    response = await test_client.put("/pharmacy/orders/1", json=test_pharmacy_order_data)
    assert response.status_code == 200
    data = response.json()
    assert data["prescription_id"] == test_pharmacy_order_data["prescription_id"]


@pytest.mark.asyncio
async def test_delete_pharmacy_order(test_client: AsyncClient):
    # Assuming an order with ID 1 exists
    response = await test_client.delete("/pharmacy/orders/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True} 