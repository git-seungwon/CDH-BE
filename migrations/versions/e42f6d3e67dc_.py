"""empty message

Revision ID: e42f6d3e67dc
Revises: 2226a171b0de
Create Date: 2024-11-24 19:09:08.097288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e42f6d3e67dc'
down_revision: Union[str, None] = '2226a171b0de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'api', 'notes', ['user_id'], ['user_id'])
    op.add_column('erd', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'erd', 'notes', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'erd', type_='foreignkey')
    op.drop_column('erd', 'user_id')
    op.drop_constraint(None, 'api', type_='foreignkey')
    # ### end Alembic commands ###
