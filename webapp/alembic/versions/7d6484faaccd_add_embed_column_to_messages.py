"""Add embed column to messages

Revision ID: 7d6484faaccd
Revises: a5780c871aec
Create Date: 2017-11-04 06:39:41.926145

"""

# revision identifiers, used by Alembic.
revision = '7d6484faaccd'
down_revision = 'a5780c871aec'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('embeds', sa.Text().with_variant(sa.Text(length=4294967295), 'mysql'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'embeds')
    # ### end Alembic commands ###