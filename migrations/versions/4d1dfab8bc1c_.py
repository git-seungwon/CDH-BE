"""empty message

Revision ID: 4d1dfab8bc1c
Revises: b1c6e50ae8af
Create Date: 2024-11-24 19:31:42.033621

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4d1dfab8bc1c'
down_revision: Union[str, None] = 'b1c6e50ae8af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'api', 'user_info', ['user_id'], ['user_id'])
    op.add_column('erd', sa.Column('user_id', sa.Integer(), nullable=False, comment='사용자 고유 아이디'))
    op.create_foreign_key(None, 'erd', 'user_info', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'erd', type_='foreignkey')
    op.drop_column('erd', 'user_id')
    op.drop_constraint(None, 'api', type_='foreignkey')
    # ### end Alembic commands ###
