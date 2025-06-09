import pytest
from src.models import Transaction, Account, OperationType
from tests.factories import TransactionFactory, AccountFactory, OperationTypeFactory


@pytest.fixture
def transaction() -> Transaction:
    return TransactionFactory()


@pytest.fixture
def account() -> Account:
    return AccountFactory()


@pytest.fixture
def operation_type() -> OperationType:
    return OperationTypeFactory()


def test_transaction_save(operation_type: OperationType, account: Account):
    operation_type.save()
    account.save()

    transaction = TransactionFactory(
        account_id=account.id,
        operation_type_id=operation_type.id,
    )

    found_transaction = transaction.save()

    assert found_transaction is not None
    assert found_transaction.id == transaction.id
    assert found_transaction.account_id == transaction.account_id
    assert found_transaction.operation_type_id == transaction.operation_type_id
    assert found_transaction.amount == transaction.amount
    assert found_transaction.created_at == transaction.created_at


def test_account_save(account: Account):
    account = account.save()

    assert account.id is not None
    assert account.document_number is not None
    assert account.created_at is not None


def test_operation_type_save(operation_type: OperationType):
    operation_type = operation_type.save()

    assert operation_type.id is not None
    assert operation_type.description is not None
    assert operation_type.slug is not None
    assert operation_type.created_at is not None
