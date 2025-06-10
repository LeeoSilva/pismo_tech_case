import fastapi
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.models import OperationTypesEnum, Account
from src.requests import CreateAccountRequest, CreateTransactionRequest
from src.repositories import (
    get_account_by_id,
    insert_account,
    insert_transaction,
    update_credit_limit,
)


router = fastapi.APIRouter(tags=["/"])


@router.get("/")
async def root() -> JSONResponse:
    return JSONResponse(
        status_code=fastapi.status.HTTP_200_OK,
        content={
            "message": "Welcome to the Pismo Tech Case API",
            "documentation_url": "/api/docs",
        },
    )


@router.post("/accounts")
async def create_account(account: CreateAccountRequest) -> JSONResponse:
    new_account = insert_account(account)
    json = jsonable_encoder(new_account)
    return JSONResponse(
        status_code=fastapi.status.HTTP_201_CREATED,
        content={
            "data": json,
        },
    )


@router.get("/accounts/{account_id}")
async def get_account(account_id: int):
    account = get_account_by_id(account_id)
    json = jsonable_encoder(account)

    if account is None:
        return JSONResponse(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            content={"message": "Account not found"},
        )

    return JSONResponse(
        status_code=fastapi.status.HTTP_200_OK,
        content={
            "data": json,
        },
    )


@router.post("/transactions")
async def create_transaction(payload: CreateTransactionRequest):
    account = get_account_by_id(payload.account_id)
    operation_type = OperationTypesEnum(payload.operation_type_id)

    # Check if transaction is valid
    if is_operation_valid(account, payload.amount, operation_type):
        transaction = insert_transaction(payload)
        update_credit_limit(
            account,
            payload.amount,
            operation_type=operation_type,
        )
    else:
        return JSONResponse(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            content={"message": "Invalid operation"},
        )

    json = jsonable_encoder(transaction)
    return JSONResponse(
        status_code=fastapi.status.HTTP_201_CREATED,
        content={
            "data": json,
        },
    )


def is_operation_valid(
    account: Account, amount: float, operation_type: OperationTypesEnum
) -> bool:
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

    account_limit = account.account_limit
    account_limit += amount

    if account.account_limit < 0:
        raise ValueError("Credit limit cannot be negative")

    return True
