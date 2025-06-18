import pytest
from httpx import AsyncClient
from app.models.lab import LabOrder, LabResult, DiagnosticImage
from app.models.user import User
from app.api.dependencies.auth import get_current_active_user


# Fixtures for test data
@pytest.fixture
def test_lab_order_data():
    return {
        "patient_id": 1,
        "doctor_id": 1,
        "order_date": "2023-01-01",
        "test_type": "blood_test",
        "priority": "routine",
        "notes": "Complete blood count"
    }


@pytest.fixture
def test_lab_result_data():
    return {
        "lab_order_id": 1,
        "result_date": "2023-01-02",
        "test_type": "blood_test",
        "results": {
            "hemoglobin": "14.2 g/dL",
            "white_blood_cells": "7.5 x10^9/L",
            "platelets": "250 x10^9/L"
        },
        "status": "completed",
        "interpretation": "Normal results"
    }


@pytest.fixture
def test_diagnostic_image_data():
    return {
        "patient_id": 1,
        "doctor_id": 1,
        "image_type": "x-ray",
        "image_date": "2023-01-01",
        "image_url": "https://example.com/images/xray123.jpg",
        "findings": "No significant abnormalities",
        "status": "completed"
    }


# Override get_current_active_user for testing
async def override_get_current_active_user():
    return User(id=1, email="test@example.com", username="testuser", is_active=True)


# Lab Order Tests
@pytest.mark.asyncio
async def test_create_lab_order(test_client: AsyncClient, test_lab_order_data):
    response = await test_client.post("/lab/orders/", json=test_lab_order_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_lab_order_data["patient_id"]


@pytest.mark.asyncio
async def test_list_lab_orders(test_client: AsyncClient):
    response = await test_client.get("/lab/orders/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_lab_order(test_client: AsyncClient):
    # Assuming an order with ID 1 exists
    response = await test_client.get("/lab/orders/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_lab_order(test_client: AsyncClient, test_lab_order_data):
    # Assuming an order with ID 1 exists
    response = await test_client.put("/lab/orders/1", json=test_lab_order_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_lab_order_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_lab_order(test_client: AsyncClient):
    # Assuming an order with ID 1 exists
    response = await test_client.delete("/lab/orders/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Lab Result Tests
@pytest.mark.asyncio
async def test_create_lab_result(test_client: AsyncClient, test_lab_result_data):
    response = await test_client.post("/lab/results/", json=test_lab_result_data)
    assert response.status_code == 200
    data = response.json()
    assert data["lab_order_id"] == test_lab_result_data["lab_order_id"]


@pytest.mark.asyncio
async def test_list_lab_results(test_client: AsyncClient):
    response = await test_client.get("/lab/results/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_lab_result(test_client: AsyncClient):
    # Assuming a result with ID 1 exists
    response = await test_client.get("/lab/results/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_lab_result(test_client: AsyncClient, test_lab_result_data):
    # Assuming a result with ID 1 exists
    response = await test_client.put("/lab/results/1", json=test_lab_result_data)
    assert response.status_code == 200
    data = response.json()
    assert data["lab_order_id"] == test_lab_result_data["lab_order_id"]


@pytest.mark.asyncio
async def test_delete_lab_result(test_client: AsyncClient):
    # Assuming a result with ID 1 exists
    response = await test_client.delete("/lab/results/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Diagnostic Image Tests
@pytest.mark.asyncio
async def test_create_diagnostic_image(test_client: AsyncClient, test_diagnostic_image_data):
    response = await test_client.post("/lab/diagnostic-images/", json=test_diagnostic_image_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_diagnostic_image_data["patient_id"]


@pytest.mark.asyncio
async def test_list_diagnostic_images(test_client: AsyncClient):
    response = await test_client.get("/lab/diagnostic-images/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_diagnostic_image(test_client: AsyncClient):
    # Assuming an image with ID 1 exists
    response = await test_client.get("/lab/diagnostic-images/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_diagnostic_image(test_client: AsyncClient, test_diagnostic_image_data):
    # Assuming an image with ID 1 exists
    response = await test_client.put("/lab/diagnostic-images/1", json=test_diagnostic_image_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_diagnostic_image_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_diagnostic_image(test_client: AsyncClient):
    # Assuming an image with ID 1 exists
    response = await test_client.delete("/lab/diagnostic-images/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True} 