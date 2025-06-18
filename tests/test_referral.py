import pytest
from httpx import AsyncClient
from app.models.referral import ReferralRequest, ReferralStatus, SpecialistNote
from app.models.user import User
from app.api.dependencies.auth import get_current_active_user


# Fixtures for test data
@pytest.fixture
def test_referral_request_data():
    return {
        "patient_id": 1,
        "referring_doctor_id": 1,
        "specialist_id": 2,
        "request_date": "2023-01-01",
        "reason": "Specialized consultation needed",
        "priority": "routine",
        "notes": "Patient requires specialized care"
    }


@pytest.fixture
def test_referral_status_data():
    return {
        "referral_request_id": 1,
        "status": "accepted",
        "update_date": "2023-01-02",
        "notes": "Specialist has accepted the referral"
    }


@pytest.fixture
def test_specialist_note_data():
    return {
        "referral_request_id": 1,
        "specialist_id": 2,
        "note_date": "2023-01-03",
        "content": "Initial assessment completed",
        "recommendations": "Schedule follow-up in 2 weeks"
    }


# Override get_current_active_user for testing
async def override_get_current_active_user():
    return User(id=1, email="test@example.com", username="testuser", is_active=True)


# Referral Request Tests
@pytest.mark.asyncio
async def test_create_referral_request(test_client: AsyncClient, test_referral_request_data):
    response = await test_client.post("/referral/requests/", json=test_referral_request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_referral_request_data["patient_id"]


@pytest.mark.asyncio
async def test_list_referral_requests(test_client: AsyncClient):
    response = await test_client.get("/referral/requests/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_referral_request(test_client: AsyncClient):
    # Assuming a request with ID 1 exists
    response = await test_client.get("/referral/requests/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_referral_request(test_client: AsyncClient, test_referral_request_data):
    # Assuming a request with ID 1 exists
    response = await test_client.put("/referral/requests/1", json=test_referral_request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_referral_request_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_referral_request(test_client: AsyncClient):
    # Assuming a request with ID 1 exists
    response = await test_client.delete("/referral/requests/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Referral Status Tests
@pytest.mark.asyncio
async def test_create_referral_status(test_client: AsyncClient, test_referral_status_data):
    response = await test_client.post("/referral/status/", json=test_referral_status_data)
    assert response.status_code == 200
    data = response.json()
    assert data["referral_request_id"] == test_referral_status_data["referral_request_id"]


@pytest.mark.asyncio
async def test_list_referral_statuses(test_client: AsyncClient):
    response = await test_client.get("/referral/status/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_referral_status(test_client: AsyncClient):
    # Assuming a status with ID 1 exists
    response = await test_client.get("/referral/status/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_referral_status(test_client: AsyncClient, test_referral_status_data):
    # Assuming a status with ID 1 exists
    response = await test_client.put("/referral/status/1", json=test_referral_status_data)
    assert response.status_code == 200
    data = response.json()
    assert data["referral_request_id"] == test_referral_status_data["referral_request_id"]


@pytest.mark.asyncio
async def test_delete_referral_status(test_client: AsyncClient):
    # Assuming a status with ID 1 exists
    response = await test_client.delete("/referral/status/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Specialist Note Tests
@pytest.mark.asyncio
async def test_create_specialist_note(test_client: AsyncClient, test_specialist_note_data):
    response = await test_client.post("/referral/specialist-notes/", json=test_specialist_note_data)
    assert response.status_code == 200
    data = response.json()
    assert data["referral_request_id"] == test_specialist_note_data["referral_request_id"]


@pytest.mark.asyncio
async def test_list_specialist_notes(test_client: AsyncClient):
    response = await test_client.get("/referral/specialist-notes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_specialist_note(test_client: AsyncClient):
    # Assuming a note with ID 1 exists
    response = await test_client.get("/referral/specialist-notes/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_specialist_note(test_client: AsyncClient, test_specialist_note_data):
    # Assuming a note with ID 1 exists
    response = await test_client.put("/referral/specialist-notes/1", json=test_specialist_note_data)
    assert response.status_code == 200
    data = response.json()
    assert data["referral_request_id"] == test_specialist_note_data["referral_request_id"]


@pytest.mark.asyncio
async def test_delete_specialist_note(test_client: AsyncClient):
    # Assuming a note with ID 1 exists
    response = await test_client.delete("/referral/specialist-notes/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True} 