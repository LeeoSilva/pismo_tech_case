"""Hidrate OperationsTypes table

Revision ID: 6aabfe1d04c8
Revises: 4d8e0de1b49d
Create Date: 2025-06-09 11:39:50.886962

"""

from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = "6aabfe1d04c8"
down_revision: Union[str, None] = "4d8e0de1b49d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

data = [
    "Normal Purchase",
    "Purchase with installments",
    "Withdrawal",
    "Credit Voucher",
]


def upgrade() -> None:
    pass
    # for description in data:
    #     operation_type = OperationType(
    #         description=description,
    #         slug=slugify.slugify(description, separator="_"),
    #         created_at=str(datetime.datetime.now(datetime.timezone.utc)),
    #     )
    #     operation_type.save()


def downgrade() -> None:
    pass
    # op.execute(f"DELETE FROM {OperationType.__tablename__}")
