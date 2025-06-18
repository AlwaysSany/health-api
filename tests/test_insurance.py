import pytest
from httpx import AsyncClient
from app.models.insurance import InsurancePlan, InsuranceClaim, Payment, Invoice
from app.models.user import User
from app.api.dependencies.auth import get_current_active_user


# Fixtures for test data
@pytest.fixture
def test_insurance_plan_data():
    return {
        "name": "Basic Health Plan",
        "provider": "HealthCare Inc",
        "coverage_details": "Covers basic medical expenses"
    }


@pytest.fixture
def test_insurance_claim_data():
    return {
        "patient_id": 1,
        "plan_id": 1,
        "claim_date": "2023-01-01",
        "amount": 1000.0,
        "status": "pending",
        "details": "Routine checkup"
    }


@pytest.fixture
def test_payment_data():
    return {
        "patient_id": 1,
        "amount": 500.0,
        "payment_date": "2023-01-15",
        "method": "credit_card",
        "invoice_id": 1
    }


@pytest.fixture
def test_invoice_data():
    return {
        "patient_id": 1,
        "total_amount": 1000.0,
        "issue_date": "2023-01-10",
        "due_date": "2023-02-10",
        "status": "unpaid",
        "details": "Medical services invoice"
    }


# Override get_current_active_user for testing
async def override_get_current_active_user():
    return User(id=1, email="test@example.com", username="testuser", is_active=True)


# Insurance Plan Tests
@pytest.mark.asyncio
async def test_create_insurance_plan(test_client: AsyncClient, test_insurance_plan_data):
    response = await test_client.post("/insurance/plans/", json=test_insurance_plan_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_insurance_plan_data["name"]


@pytest.mark.asyncio
async def test_list_insurance_plans(test_client: AsyncClient):
    response = await test_client.get("/insurance/plans/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_insurance_plan(test_client: AsyncClient):
    # Assuming a plan with ID 1 exists
    response = await test_client.get("/insurance/plans/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_insurance_plan(test_client: AsyncClient, test_insurance_plan_data):
    # Assuming a plan with ID 1 exists
    response = await test_client.put("/insurance/plans/1", json=test_insurance_plan_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_insurance_plan_data["name"]


@pytest.mark.asyncio
async def test_delete_insurance_plan(test_client: AsyncClient):
    # Assuming a plan with ID 1 exists
    response = await test_client.delete("/insurance/plans/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Insurance Claim Tests
@pytest.mark.asyncio
async def test_create_insurance_claim(test_client: AsyncClient, test_insurance_claim_data):
    response = await test_client.post("/insurance/claims/", json=test_insurance_claim_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_insurance_claim_data["patient_id"]


@pytest.mark.asyncio
async def test_list_insurance_claims(test_client: AsyncClient):
    response = await test_client.get("/insurance/claims/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_insurance_claim(test_client: AsyncClient):
    # Assuming a claim with ID 1 exists
    response = await test_client.get("/insurance/claims/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_insurance_claim(test_client: AsyncClient, test_insurance_claim_data):
    # Assuming a claim with ID 1 exists
    response = await test_client.put("/insurance/claims/1", json=test_insurance_claim_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_insurance_claim_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_insurance_claim(test_client: AsyncClient):
    # Assuming a claim with ID 1 exists
    response = await test_client.delete("/insurance/claims/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Payment Tests
@pytest.mark.asyncio
async def test_create_payment(test_client: AsyncClient, test_payment_data):
    response = await test_client.post("/insurance/payments/", json=test_payment_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_payment_data["patient_id"]


@pytest.mark.asyncio
async def test_list_payments(test_client: AsyncClient):
    response = await test_client.get("/insurance/payments/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_payment(test_client: AsyncClient):
    # Assuming a payment with ID 1 exists
    response = await test_client.get("/insurance/payments/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_payment(test_client: AsyncClient, test_payment_data):
    # Assuming a payment with ID 1 exists
    response = await test_client.put("/insurance/payments/1", json=test_payment_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_payment_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_payment(test_client: AsyncClient):
    # Assuming a payment with ID 1 exists
    response = await test_client.delete("/insurance/payments/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Invoice Tests
@pytest.mark.asyncio
async def test_create_invoice(test_client: AsyncClient, test_invoice_data):
    response = await test_client.post("/insurance/invoices/", json=test_invoice_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_invoice_data["patient_id"]


@pytest.mark.asyncio
async def test_list_invoices(test_client: AsyncClient):
    response = await test_client.get("/insurance/invoices/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_invoice(test_client: AsyncClient):
    # Assuming an invoice with ID 1 exists
    response = await test_client.get("/insurance/invoices/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_invoice(test_client: AsyncClient, test_invoice_data):
    # Assuming an invoice with ID 1 exists
    response = await test_client.put("/insurance/invoices/1", json=test_invoice_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_invoice_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_invoice(test_client: AsyncClient):
    # Assuming an invoice with ID 1 exists
    response = await test_client.delete("/insurance/invoices/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True} 