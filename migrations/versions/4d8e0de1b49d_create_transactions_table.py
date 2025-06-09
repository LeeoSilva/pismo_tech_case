"""Create Transactions table

Revision ID: 4d8e0de1b49d
Revises: bdbd1adc7f86
Create Date: 2025-06-09 09:38:44.050755

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.sql.functions import current_timestamp
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4d8e0de1b49d"
down_revision: Union[str, None] = "bdbd1adc7f86"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
table_name: str = "transactions"


def upgrade() -> None:
    op.create_table(
        table_name,
        sa.Column(
            "id",
            sa.Integer,
            primary_key=True,
            autoincrement=True,
            index=True,
            nullable=False,
        ),
        sa.Column("account_id", sa.Integer, nullable=False),
        sa.Column("operation_type_id", sa.Integer, nullable=False),
        sa.Column("amount", sa.DECIMAL(precision=19, scale=2), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            server_default=current_timestamp(),
        ),
    )


def downgrade() -> None:
    op.drop_table(table_name)
