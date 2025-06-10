import fastapi
from src.repositories import get_account_limit
from src.models import OperationTypesEnum
from src.main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_create_account(client: TestClient):
    response = client.post(
        "/api/accounts",
        json={
            "document_number": "123456789",
            "account_limit": 1000.0,
        },
    )
    assert response.status_code == fastapi.status.HTTP_201_CREATED


def test_get_account(client: TestClient):
    create_response = client.post(
        "/api/accounts",
        json={
            "document_number": "987654321",
            "account_limit": 500.0,
        },
    )
    assert create_response.status_code == fastapi.status.HTTP_201_CREATED
    account_id = create_response.json()["data"]["id"]

    response = client.get(f"/api/accounts/{account_id}")
    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json()["data"]["id"] == account_id


def test_create_transaction(client: TestClient):
    create_account_response = client.post(
        "/api/accounts",
        json={
            "document_number": "123456789",
            "account_limit": 1000.0,
        },
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


def test_multiple_transactions_equal_zero(client: TestClient):
    create_account_response = client.post(
        "/api/accounts",
        json={
            "document_number": "123456789",
            "account_limit": 100.0,
        },
    )
    assert create_account_response.status_code == fastapi.status.HTTP_201_CREATED
    account_id = create_account_response.json()["data"]["id"]

    # First transaction
    response = client.post(
        "/api/transactions",
        json={
            "account_id": account_id,
            "operation_type_id": OperationTypesEnum.WITHDRAWAL.value,
            "amount": 50.0,
        },
    )
    assert response.status_code == fastapi.status.HTTP_201_CREATED

    # Second transaction
    response = client.post(
        "/api/transactions",
        json={
            "account_id": account_id,
            "operation_type_id": OperationTypesEnum.WITHDRAWAL.value,
            "amount": 50.0,
        },
    )
    assert response.status_code == fastapi.status.HTTP_201_CREATED
    account_limit = get_account_limit(account_id)
    expected_acount_limit = 0

    assert account_limit == expected_acount_limit
