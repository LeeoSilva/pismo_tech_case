"""Add account_limit to Accounts table

Revision ID: 418920596455
Revises: 6aabfe1d04c8
Create Date: 2025-06-10 10:57:59.306611

"""

from typing import Sequence, Union

from alembic import op
import sqlmodel as sm


# revision identifiers, used by Alembic.
revision: str = "418920596455"
down_revision: Union[str, None] = "6aabfe1d04c8"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
table_name: str = "accounts"


def upgrade() -> None:
    op.add_column(
        table_name,
        sm.Column(
            "account_limit",
            sm.DECIMAL(
                precision=19,
                scale=2,
            ),
            nullable=True,
        ),
    )


def downgrade() -> None:
    op.drop_column(table_name, "account_limit")
