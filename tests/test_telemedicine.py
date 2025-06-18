import pytest
from httpx import AsyncClient
from app.models.telemedicine import VirtualVisit, ChatLog, VideoSession
from app.models.user import User
from app.api.dependencies.auth import get_current_active_user


# Fixtures for test data
@pytest.fixture
def test_virtual_visit_data():
    return {
        "patient_id": 1,
        "doctor_id": 1,
        "visit_date": "2023-01-01T10:00:00",
        "status": "scheduled",
        "visit_type": "video",
        "notes": "Follow-up consultation"
    }


@pytest.fixture
def test_chat_log_data():
    return {
        "patient_id": 1,
        "doctor_id": 1,
        "message": "Hello, how are you feeling today?",
        "timestamp": "2023-01-01T10:05:00",
        "sender_type": "doctor"
    }


@pytest.fixture
def test_video_session_data():
    return {
        "virtual_visit_id": 1,
        "start_time": "2023-01-01T10:00:00",
        "end_time": "2023-01-01T10:30:00",
        "status": "completed",
        "quality_metrics": {"resolution": "1080p", "latency": "50ms"}
    }


# Override get_current_active_user for testing
async def override_get_current_active_user():
    return User(id=1, email="test@example.com", username="testuser", is_active=True)


# Virtual Visit Tests
@pytest.mark.asyncio
async def test_create_virtual_visit(test_client: AsyncClient, test_virtual_visit_data):
    response = await test_client.post("/telemedicine/visits/", json=test_virtual_visit_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_virtual_visit_data["patient_id"]


@pytest.mark.asyncio
async def test_list_virtual_visits(test_client: AsyncClient):
    response = await test_client.get("/telemedicine/visits/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_virtual_visit(test_client: AsyncClient):
    # Assuming a visit with ID 1 exists
    response = await test_client.get("/telemedicine/visits/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_virtual_visit(test_client: AsyncClient, test_virtual_visit_data):
    # Assuming a visit with ID 1 exists
    response = await test_client.put("/telemedicine/visits/1", json=test_virtual_visit_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_virtual_visit_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_virtual_visit(test_client: AsyncClient):
    # Assuming a visit with ID 1 exists
    response = await test_client.delete("/telemedicine/visits/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Chat Log Tests
@pytest.mark.asyncio
async def test_create_chat_log(test_client: AsyncClient, test_chat_log_data):
    response = await test_client.post("/telemedicine/chat-logs/", json=test_chat_log_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_chat_log_data["patient_id"]


@pytest.mark.asyncio
async def test_list_chat_logs(test_client: AsyncClient):
    response = await test_client.get("/telemedicine/chat-logs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_chat_log(test_client: AsyncClient):
    # Assuming a chat log with ID 1 exists
    response = await test_client.get("/telemedicine/chat-logs/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_chat_log(test_client: AsyncClient, test_chat_log_data):
    # Assuming a chat log with ID 1 exists
    response = await test_client.put("/telemedicine/chat-logs/1", json=test_chat_log_data)
    assert response.status_code == 200
    data = response.json()
    assert data["patient_id"] == test_chat_log_data["patient_id"]


@pytest.mark.asyncio
async def test_delete_chat_log(test_client: AsyncClient):
    # Assuming a chat log with ID 1 exists
    response = await test_client.delete("/telemedicine/chat-logs/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


# Video Session Tests
@pytest.mark.asyncio
async def test_create_video_session(test_client: AsyncClient, test_video_session_data):
    response = await test_client.post("/telemedicine/video-sessions/", json=test_video_session_data)
    assert response.status_code == 200
    data = response.json()
    assert data["virtual_visit_id"] == test_video_session_data["virtual_visit_id"]


@pytest.mark.asyncio
async def test_list_video_sessions(test_client: AsyncClient):
    response = await test_client.get("/telemedicine/video-sessions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_get_video_session(test_client: AsyncClient):
    # Assuming a video session with ID 1 exists
    response = await test_client.get("/telemedicine/video-sessions/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


@pytest.mark.asyncio
async def test_update_video_session(test_client: AsyncClient, test_video_session_data):
    # Assuming a video session with ID 1 exists
    response = await test_client.put("/telemedicine/video-sessions/1", json=test_video_session_data)
    assert response.status_code == 200
    data = response.json()
    assert data["virtual_visit_id"] == test_video_session_data["virtual_visit_id"]


@pytest.mark.asyncio
async def test_delete_video_session(test_client: AsyncClient):
    # Assuming a video session with ID 1 exists
    response = await test_client.delete("/telemedicine/video-sessions/1")
    assert response.status_code == 200
    assert response.json() == {"ok": True} 