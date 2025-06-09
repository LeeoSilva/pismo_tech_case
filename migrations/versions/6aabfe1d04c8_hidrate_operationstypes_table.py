"""Hidrate OperationsTypes table

Revision ID: 6aabfe1d04c8
Revises: 4d8e0de1b49d
Create Date: 2025-06-09 11:39:50.886962

"""

from typing import Sequence, Union
import datetime

from alembic import op
import sqlmodel as sm
import slugify


# revision identifiers, used by Alembic.
revision: str = "6aabfe1d04c8"
down_revision: Union[str, None] = "4d8e0de1b49d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
table_name: str = "operation_types"

data = [
    "Normal Purchase",
    "Purchase with installments",
    "Withdrawal",
    "Credit Voucher",
]


def upgrade() -> None:
    conn = op.get_bind()

    rows = [
        {
            "description": description,
            "slug": slugify.slugify(description),
            "created_at": datetime.datetime.now(datetime.timezone.utc),
        }
        for description in data
    ]

    conn.execute(
        sm.text(
            f"""
                INSERT INTO {table_name} (description, slug, created_at)
                VALUES (:description, :slug, :created_at)
            """
        ),
        rows,
    )


def downgrade() -> None:
    op.execute(f"DELETE FROM {table_name}")
