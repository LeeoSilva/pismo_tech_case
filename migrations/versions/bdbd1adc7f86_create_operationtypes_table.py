"""Create OperationTypes table

Revision ID: bdbd1adc7f86
Revises: 478919eca5f9
Create Date: 2025-06-09 09:38:34.779294

"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bdbd1adc7f86"
down_revision: Union[str, None] = "478919eca5f9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
table_name: str = "operation_types"


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
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("slug", sa.String(), nullable=False, unique=True),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.current_timestamp(),
        ),
    )


def downgrade() -> None:
    op.drop_table(table_name)
