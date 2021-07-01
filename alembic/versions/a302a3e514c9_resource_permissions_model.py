"""Resource permissions model

Revision ID: a302a3e514c9
Revises: 1ff0db1a7b28
Create Date: 2021-05-14 08:46:42.024938

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a302a3e514c9'
down_revision = '1ff0db1a7b28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resources',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_resources')),
    sa.UniqueConstraint('id', name=op.f('uq_resources_id'))
    )
    op.create_table('resource_permissions',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('resource_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('permission', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], name=op.f('fk_resource_permissions_resource_id_resources'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_resource_permissions')),
    sa.UniqueConstraint('id', name=op.f('uq_resource_permissions_id'))
    )
    op.create_table('resource_holder_permissions',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('group_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('resource_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('permission_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], name=op.f('fk_resource_holder_permissions_group_id_groups'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['permission_id'], ['resource_permissions.id'], name=op.f('fk_resource_holder_permissions_permission_id_resource_permissions'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], name=op.f('fk_resource_holder_permissions_resource_id_resources'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_resource_holder_permissions_user_id_users'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_resource_holder_permissions')),
    sa.UniqueConstraint('id', name=op.f('uq_resource_holder_permissions_id')),
    sa.UniqueConstraint('user_id', 'group_id', 'resource_id', 'permission_id', name=op.f('uq_resource_holder_permissions_user_id'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resource_holder_permissions')
    op.drop_table('resource_permissions')
    op.drop_table('resources')
    # ### end Alembic commands ###
