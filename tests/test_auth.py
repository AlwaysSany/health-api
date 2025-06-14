import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register_user(test_client: AsyncClient, test_user_data):
    """Test user registration."""
    response = await test_client.post("/auth/register", json=test_user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user_data["email"]
    assert data["username"] == test_user_data["username"]
    assert "id" in data


@pytest.mark.asyncio
async def test_register_duplicate_user(test_client: AsyncClient, test_user_data):
    """Test duplicate user registration."""
    # Register user first time
    await test_client.post("/auth/register", json=test_user_data)

    # Try to register same user again
    response = await test_client.post("/auth/register", json=test_user_data)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_login_user(test_client: AsyncClient, test_user_data):
    """Test user login."""
    # Register user first
    await test_client.post("/auth/register", json=test_user_data)

    # Login
    login_data = {
        "username": test_user_data["username"],
        "password": test_user_data["password"],
    }
    response = await test_client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_invalid_credentials(test_client: AsyncClient):
    """Test login with invalid credentials."""
    login_data = {"username": "nonexistent", "password": "wrongpassword"}
    response = await test_client.post("/auth/login", data=login_data)
    assert response.status_code == 401
