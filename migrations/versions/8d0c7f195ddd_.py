"""empty message

Revision ID: 8d0c7f195ddd
Revises: fdf649edb89c
Create Date: 2024-11-28 13:15:00.924057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d0c7f195ddd'
down_revision: Union[str, None] = 'fdf649edb89c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='PK'),
    sa.Column('invite_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False, comment='사용자 고유 아이디'),
    sa.Column('nickname', sa.String(length=20), nullable=False),
    sa.Column('joined_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['invite_id'], ['group.invite_id'], ),
    sa.ForeignKeyConstraint(['nickname'], ['user_info.nickname'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member')
    # ### end Alembic commands ###
