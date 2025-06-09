"""Create Accounts table

Revision ID: 478919eca5f9
Revises:
Create Date: 2025-06-09 09:38:18.041269

"""

from typing import Sequence, Union
import sqlmodel as sm

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
        sm.Column(
            "id",
            sm.Integer,
            primary_key=True,
            autoincrement=True,
            index=True,
            nullable=False,
        ),
        sm.Column("document_number", sm.String(), nullable=False),
        sm.Column(
            "created_at",
            sm.DateTime,
            nullable=False,
            server_default=sm.func.current_timestamp(),
        ),
    )


def downgrade() -> None:
    op.drop_table(table_name)
