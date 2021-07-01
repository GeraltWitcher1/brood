"""Group autogenerated and token type

Revision ID: 84e5ee946489
Revises: d244ea9f09df
Create Date: 2020-11-19 07:10:21.034303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84e5ee946489'
down_revision = 'd244ea9f09df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groups', sa.Column('autogenerated', sa.Boolean(), nullable=True))
    op.add_column('tokens', sa.Column('note', sa.String(), nullable=True))

    # Manual
    sa.Enum('bugout', 'slack', 'github', name='token_type').create(op.get_bind())
    op.add_column('tokens', sa.Column('token_type', sa.Enum('bugout', 'slack', 'github', name='token_type'), nullable=True))

    op.execute("UPDATE groups SET autogenerated = false")
    op.alter_column("groups", "autogenerated", nullable=False)

    op.execute("UPDATE tokens SET token_type = 'bugout'")
    op.alter_column("tokens", "token_type", nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tokens', 'token_type')
    op.drop_column('tokens', 'note')
    op.drop_column('groups', 'autogenerated')

    # Manual
    sa.Enum('bugout', 'slack', 'github', name='token_type').drop(op.get_bind(), checkfirst=False)
    # ### end Alembic commands ###
