"""Restricted tokens

Revision ID: d9cfbdd09cc7
Revises: ea9c6f4e526f
Create Date: 2021-02-24 22:31:32.485820

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "d9cfbdd09cc7"
down_revision = "ea9c6f4e526f"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("tokens", sa.Column("restricted", sa.Boolean(), nullable=True))
    op.execute("UPDATE tokens set restricted = false;")
    op.alter_column("tokens", "restricted", nullable=False)
    op.create_index(
        op.f("ix_tokens_restricted"), "tokens", ["restricted"], unique=False
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tokens_restricted"), table_name="tokens")
    op.drop_column("tokens", "restricted")
    # ### end Alembic commands ###
