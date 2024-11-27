"""empty message

Revision ID: 58acb15d44b9
Revises: 4d1dfab8bc1c
Create Date: 2024-11-24 19:31:59.580696

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '58acb15d44b9'
down_revision: Union[str, None] = '4d1dfab8bc1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('api', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=True,
               existing_comment='노트의 사용자 고유 아이디')
    op.create_foreign_key(None, 'api', 'user_info', ['user_id'], ['user_id'])
    op.add_column('erd', sa.Column('user_id', sa.Integer(), nullable=True, comment='사용자 고유 아이디'))
    op.create_foreign_key(None, 'erd', 'user_info', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'erd', type_='foreignkey')
    op.drop_column('erd', 'user_id')
    op.drop_constraint(None, 'api', type_='foreignkey')
    op.alter_column('api', 'user_id',
               existing_type=mysql.INTEGER(),
               nullable=False,
               existing_comment='노트의 사용자 고유 아이디')
    # ### end Alembic commands ###