import asyncio
import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database.base import Base
from app.api.dependencies.database import get_async_session
from app.core.config import settings

# Test database URL (use in-memory SQLite for tests)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture
async def test_engine():
    """Create test database engine."""
    engine = create_async_engine(
        TEST_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()


@pytest_asyncio.fixture
async def test_session(test_engine):
    """Create test database session."""
    async_session = async_sessionmaker(
        test_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session


@pytest_asyncio.fixture
async def test_client(test_session):
    """Create test client with dependency overrides."""

    async def override_get_db():
        yield test_session

    app.dependency_overrides[get_async_session] = override_get_db

    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def test_user_data():
    """Test user data."""
    return {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123",
    }


@pytest.fixture
def test_patient_data():
    """Test patient data."""
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "date_of_birth": "1990-01-01",
        "gender": "male",
        "address": "123 Main St, City, State",
        "emergency_contact_name": "Jane Doe",
        "emergency_contact_phone": "+1234567891",
    }


@pytest.fixture
def test_doctor_data():
    """Test doctor data."""
    return {
        "first_name": "Dr. Sarah",
        "last_name": "Smith",
        "email": "dr.smith@hospital.com",
        "phone": "+1234567892",
        "specialization": "Cardiology",
        "license_number": "MD123456",
        "years_of_experience": 10,
        "bio": "Experienced cardiologist",
    }
