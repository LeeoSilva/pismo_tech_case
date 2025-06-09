import fastapi
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from src.requests import CreateAccountRequest, CreateTransactionRequest
from src.repositories import get_account_by_id, insert_account


router = fastapi.APIRouter(tags=["/"])


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
    
