import fastapi
from src.main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> TestClient:
    """Fixture to create a test client for the FastAPI app."""
    return TestClient(app)


def test_create_account(client: TestClient):
    """Test the create account endpoint."""
    response = client.post(
        "/api/v1/accounts",
        json={"document_number": "123456789"},
    )
    assert response.status_code == fastapi.status.HTTP_201_CREATED


def test_get_account(client: TestClient):
    """Test the get account by ID endpoint."""
    # First, create an account to retrieve
    create_response = client.post(
        "/api/v1/accounts",
        json={"document_number": "987654321"},
    )
    assert create_response.status_code == fastapi.status.HTTP_201_CREATED
    account_id = create_response.json()["data"]["id"]

    # Now, retrieve the account by ID
    response = client.get(f"/api/v1/accounts/{account_id}")
    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json()["data"]["id"] == account_id
