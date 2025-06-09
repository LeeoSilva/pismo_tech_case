import pydantic


class CreateAccountRequest(pydantic.BaseModel):
    document_number: str


class CreateTransactionRequest(pydantic.BaseModel):
    account_id: int
    operation_type_id: int
    amount: float
