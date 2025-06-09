"""Create OperationTypes table

Revision ID: bdbd1adc7f86
Revises: 478919eca5f9
Create Date: 2025-06-09 09:38:34.779294

"""

from typing import Sequence, Union
from alembic import op
import sqlmodel as sm


# revision identifiers, used by Alembic.
revision: str = "bdbd1adc7f86"
down_revision: Union[str, None] = "478919eca5f9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
table_name: str = "operation_types"


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
        sm.Column("description", sm.String(), nullable=False),
        sm.Column("slug", sm.String(), nullable=False, unique=True),
        sm.Column(
            "created_at",
            sm.DateTime,
            nullable=False,
            server_default=sm.func.current_timestamp(),
        ),
    )


def downgrade() -> None:
    op.drop_table(table_name)
