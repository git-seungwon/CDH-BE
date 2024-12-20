"""empty message

Revision ID: 8dbcebaae654
Revises: bd402063605b
Create Date: 2024-11-30 12:57:54.151727

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8dbcebaae654'
down_revision: Union[str, None] = 'bd402063605b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notes', sa.Column('teamspace_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'notes', 'group', ['teamspace_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notes', type_='foreignkey')
    op.drop_column('notes', 'teamspace_id')
    # ### end Alembic commands ###
