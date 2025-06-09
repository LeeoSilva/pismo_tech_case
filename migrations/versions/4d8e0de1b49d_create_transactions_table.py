"""Create Transactions table

Revision ID: 4d8e0de1b49d
Revises: bdbd1adc7f86
Create Date: 2025-06-09 09:38:44.050755

"""

from typing import Sequence, Union

from alembic import op
from sqlalchemy.sql.functions import current_timestamp
import sqlmodel as sm


# revision identifiers, used by Alembic.
revision: str = "4d8e0de1b49d"
down_revision: Union[str, None] = "bdbd1adc7f86"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
table_name: str = "transactions"


def upgrade() -> None:
    op.create_table(
        table_name,
        sm.Column(
            "id",
            sm.Integer,
            primary_key=True,
            autoincrement=True,
            index=True,
            nullable=False,
        ),
        sm.Column("account_id", sm.Integer, nullable=False),
        sm.Column("operation_type_id", sm.Integer, nullable=False),
        sm.Column("amount", sm.DECIMAL(precision=19, scale=2), nullable=False),
        sm.Column(
            "created_at",
            sm.DateTime,
            nullable=False,
            server_default=current_timestamp(),
        ),
    )


def downgrade() -> None:
    op.drop_table(table_name)
