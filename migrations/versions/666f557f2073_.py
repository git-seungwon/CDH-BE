"""empty message

Revision ID: 666f557f2073
Revises: 900507c09366
Create Date: 2024-11-23 12:58:57.370551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '666f557f2073'
down_revision: Union[str, None] = '900507c09366'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin_logs', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=True)
    op.alter_column('agreement', 'create_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=True,
               existing_comment='생성 시각')
    op.alter_column('api', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=True,
               comment=None,
               existing_comment='자동',
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('calenders', 'create_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=True)
    op.alter_column('erd', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=True)
    op.alter_column('login_log', 'login_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=True,
               existing_comment='로그인 시각')
    op.alter_column('sign_up_log', 'sign_up_datetime',
               existing_type=mysql.TIMESTAMP(),
               nullable=True,
               existing_comment='회원 가입 일시')
    op.alter_column('user_info', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=True,
               comment=None,
               existing_comment='자동')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_info', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=False,
               comment='자동')
    op.alter_column('sign_up_log', 'sign_up_datetime',
               existing_type=mysql.TIMESTAMP(),
               nullable=False,
               existing_comment='회원 가입 일시')
    op.alter_column('login_log', 'login_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=False,
               existing_comment='로그인 시각')
    op.alter_column('erd', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=False)
    op.alter_column('calenders', 'create_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=False)
    op.alter_column('api', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=False,
               comment='자동',
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('agreement', 'create_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=False,
               existing_comment='생성 시각')
    op.alter_column('admin_logs', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###
