"""Create Accounts table

Revision ID: 478919eca5f9
Revises:
Create Date: 2025-06-09 09:38:18.041269

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "478919eca5f9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

table_name: str = "accounts"


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
        sa.Column("document_number", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.current_timestamp(),
        ),
    )


def downgrade() -> None:
    op.drop_table(table_name)
