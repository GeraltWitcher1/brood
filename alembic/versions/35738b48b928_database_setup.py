"""database setup

Revision ID: 35738b48b928
Revises: 
Create Date: 2020-07-20 15:13:52.429117

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '35738b48b928'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('normalized_email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('auth_type', sa.String(length=50), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_users_normalized_email'), 'users', ['normalized_email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_index(op.f('ix_users_verified'), 'users', ['verified'], unique=False)
    op.create_table('tokens',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_tokens_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tokens_active'), 'tokens', ['active'], unique=False)
    op.create_index(op.f('ix_tokens_id'), 'tokens', ['id'], unique=True)
    op.create_table('verification_emails',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('verification_code', sa.String(length=6), nullable=True),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', statement_timestamp())"), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_verification_emails_user_id'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_verification_emails_active'), 'verification_emails', ['active'], unique=False)
    op.create_index(op.f('ix_verification_emails_user_id'), 'verification_emails', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_verification_emails_user_id'), table_name='verification_emails')
    op.drop_index(op.f('ix_verification_emails_active'), table_name='verification_emails')
    op.drop_table('verification_emails')
    op.drop_index(op.f('ix_tokens_id'), table_name='tokens')
    op.drop_index(op.f('ix_tokens_active'), table_name='tokens')
    op.drop_table('tokens')
    op.drop_index(op.f('ix_users_verified'), table_name='users')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_normalized_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
