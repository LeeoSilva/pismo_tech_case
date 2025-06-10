import fastapi
from src.main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_create_account(client: TestClient):
    response = client.post(
        "/api/accounts",
        json={"document_number": "123456789"},
    )
    assert response.status_code == fastapi.status.HTTP_201_CREATED


def test_get_account(client: TestClient):
    create_response = client.post(
        "/api/accounts",
        json={"document_number": "987654321"},
    )
    assert create_response.status_code == fastapi.status.HTTP_201_CREATED
    account_id = create_response.json()["data"]["id"]

    response = client.get(f"/api/accounts/{account_id}")
    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json()["data"]["id"] == account_id

def test_create_transaction(client: TestClient):
    create_account_response = client.post(
        "/api/accounts",
        json={"document_number": "123456789"},
    )
    assert create_account_response.status_code == fastapi.status.HTTP_201_CREATED
    account_id = create_account_response.json()["data"]["id"]

    response = client.post(
        "/api/transactions",
        json={
            "account_id": account_id,
            "operation_type_id": 1,
            "amount": 100.0,
        },
    )
    assert response.status_code == fastapi.status.HTTP_201_CREATED
    assert response.json()["data"]["account_id"] == account_id