import pytest
from src.models import Account, OperationTypesEnum
from tests.factories import AccountFactory
from src.repositories import get_account_limit, update_credit_limit


@pytest.fixture
def account() -> Account:
    return AccountFactory(account_limit=1000.0)


def test_get_account_limit(account):
    account.save()

    limit = get_account_limit(account.id)

    assert limit == 1000.0


def test_update_increase_credit_limit(account):
    account.save()

    updated_account = update_credit_limit(
        account, 500, operation_type=OperationTypesEnum.CREDIT_VOUCHER
    )

    expected_new_limit = 1500.0

    assert updated_account.account_limit == expected_new_limit


def test_get_account_limit_negative_limit(account):
    account.save()  # credit_limit = 1000

    with pytest.raises(ValueError):
        update_credit_limit(account.id, -2000, operation_type=1)
