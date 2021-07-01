"""External unique column for resources

Revision ID: 02395c3b0f59
Revises: a302a3e514c9
Create Date: 2021-05-23 17:30:50.427937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02395c3b0f59'
down_revision = 'a302a3e514c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('resources', sa.Column('external', sa.String(), nullable=True))
    op.create_unique_constraint(op.f('uq_resources_external'), 'resources', ['external'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_resources_external'), 'resources', type_='unique')
    op.drop_column('resources', 'external')
    # ### end Alembic commands ###
