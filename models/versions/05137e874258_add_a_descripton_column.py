"""add a Descripton Column

Revision ID: 05137e874258
Revises: e105a217ec6e
Create Date: 2017-11-22 01:16:37.815153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05137e874258'
down_revision = 'e105a217ec6e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', 
        sa.Column('description', sa.Unicode(200), nullable=True), 
    )

def downgrade():
    op.drop_column('users', 
        'description', 
    )

