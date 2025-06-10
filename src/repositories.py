from src.requests import CreateAccountRequest, CreateTransactionRequest
from src.models import Account, Transaction


def insert_account(account: CreateAccountRequest):
    new_account = Account(document_number=account.document_number)
    return new_account.save()


def get_account_by_id(account_id: int) -> Account | None:
    return Account.find_by_id(account_id)


def insert_transaction(payload: CreateTransactionRequest):
    new_transaction = Transaction(
        account_id=payload.account_id,
        operation_type_id=payload.operation_type_id,
        amount=payload.amount,
    )
    return new_transaction.save()
