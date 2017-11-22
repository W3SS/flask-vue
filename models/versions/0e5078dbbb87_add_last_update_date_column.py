"""add last_update_date column

Revision ID: 0e5078dbbb87
Revises: 05137e874258
Create Date: 2017-11-22 04:03:46.510562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e5078dbbb87'
down_revision = '05137e874258'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('last_upate_date', sa.DateTime, nullable=True))

def downgrade():
    op.drop_column('users', 'last_update_date')
