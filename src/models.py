import enum
from typing import Self
import sqlmodel
import datetime

from src.utils import build_connection_string


engine = sqlmodel.create_engine(
    url=build_connection_string(),
    echo=True,
)


class OperationTypesEnum(enum.Enum):
    NORMAL_PURCHASE = 1  # Decrease credit limit
    INSTALLMENT_PURCHASE = 2  # Decrease credit limit
    WITHDRAWAL = 3  # Decrease credit limit
    CREDIT_VOUCHER = 4  # Increase credit limit


class BaseModel(sqlmodel.SQLModel):
    created_at: datetime.datetime = sqlmodel.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc), index=True
    )

    def save(self) -> Self:
        """Method to save the model instance to the database."""
        with sqlmodel.Session(engine) as session:
            session.add(self)
            session.commit()
            session.refresh(self)

            return self

    @classmethod
    def find_by_id(cls, id: int) -> Self:
        """Method to find an instance by its ID."""
        with sqlmodel.Session(engine) as session:
            return session.get(cls, id)


class Transaction(BaseModel, table=True):
    __tablename__ = "transactions"

    id: int = sqlmodel.Field(primary_key=True, index=True)
    account_id: int = sqlmodel.Field(foreign_key="accounts.id", nullable=False)
    operation_type_id: int = sqlmodel.Field(
        foreign_key="operation_types.id", nullable=False
    )
    amount: float = sqlmodel.Field(nullable=False)
    created_at: datetime.datetime = sqlmodel.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc), index=True
    )


class Account(BaseModel, table=True):
    __tablename__ = "accounts"

    id: int = sqlmodel.Field(primary_key=True, index=True)
    document_number: str = sqlmodel.Field(nullable=False, unique=True)
    account_limit: float = sqlmodel.Field(nullable=False)
    created_at: datetime.datetime = sqlmodel.Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc), index=True
    )


class OperationType(BaseModel, table=True):
    __tablename__ = "operation_types"

    id: int = sqlmodel.Field(primary_key=True, index=True)
    description: str = sqlmodel.Field(nullable=False, unique=True)
    slug: str = sqlmodel.Field(nullable=False, unique=True)
    created_at: datetime.datetime = sqlmodel.Field(
        default_factory=datetime.datetime.now(datetime.timezone.utc), index=True
    )

    @classmethod
    def find_by_slug(cls, slug: str) -> Self:
        """Method to find an operation type by its slug."""
        with cls.query() as session:
            session.get(cls, slug=slug)
