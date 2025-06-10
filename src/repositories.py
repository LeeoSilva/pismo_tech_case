from src.requests import CreateAccountRequest, CreateTransactionRequest
from src.models import Account, OperationTypesEnum, Transaction


def insert_account(account: CreateAccountRequest):
    new_account = Account(
        document_number=account.document_number,
        account_limit=account.account_limit,
    )
    return new_account.save()


def get_account_by_id(account_id: int) -> Account:
    account = Account.find_by_id(account_id)
    if account is None:
        raise Exception("Account not found")

    return account


def update_credit_limit(
    account: Account, amount: float, operation_type: OperationTypesEnum
) -> Account:
    if amount < 0:
        raise ValueError("Amount must be positive")

    if operation_type == OperationTypesEnum.WITHDRAWAL:
        amount = amount * -1
    elif operation_type not in [
        OperationTypesEnum.CREDIT_VOUCHER,
        OperationTypesEnum.NORMAL_PURCHASE,
        OperationTypesEnum.INSTALLMENT_PURCHASE,
    ]:
        raise ValueError("Invalid operation type")

    account.account_limit += amount

    if account.account_limit < 0:
        raise ValueError("Credit limit cannot be negative")

    return account.save()


def get_account_limit(account_id: int) -> float:
    account = get_account_by_id(account_id)
    if account is None:
        return 0

    return account.account_limit


def insert_transaction(payload: CreateTransactionRequest):
    new_transaction = Transaction(
        account_id=payload.account_id,
        operation_type_id=payload.operation_type_id,
        amount=payload.amount,
    )
    return new_transaction.save()
