"""create user model

Revision ID: e105a217ec6e
Revises: 
Create Date: 2017-11-22 01:08:19.595431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e105a217ec6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('password', sa.String(50), nullable=True)
    )


def downgrade():
    op.drop_table('users')
