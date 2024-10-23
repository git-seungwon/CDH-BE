"""empty message

Revision ID: c18aab884525
Revises: f9e9a079affd
Create Date: 2024-10-14 00:04:22.529479

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c18aab884525'
down_revision: Union[str, None] = 'f9e9a079affd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_info',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('admin_name', sa.String(length=20), nullable=False),
    sa.Column('admin_email', sa.String(length=320), nullable=False),
    sa.Column('admin_pwd', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('user_info',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False, comment='자동생성'),
    sa.Column('nickname', sa.String(length=20), nullable=True),
    sa.Column('pwd', sa.String(length=60), nullable=False, comment='암호화'),
    sa.Column('email', sa.String(length=320), nullable=True),
    sa.Column('gender', sa.Boolean(), nullable=False, comment='True 이면 남자, False 이면 여자'),
    sa.Column('created_at', sa.DateTime(), nullable=False, comment='자동'),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('admin_logs',
    sa.Column('log_id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('target_table', sa.String(length=199), nullable=False),
    sa.Column('action', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('target_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['admin_info.admin_id'], ),
    sa.PrimaryKeyConstraint('log_id')
    )
    op.create_table('notes',
    sa.Column('note_id', sa.Integer(), autoincrement=True, nullable=False, comment='자동생성'),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False, comment='자동'),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.user_id'], ),
    sa.PrimaryKeyConstraint('note_id')
    )
    op.create_table('settings',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('user_id2', sa.Integer(), nullable=False),
    sa.Column('theme', sa.String(length=7), nullable=False, comment='Hex color'),
    sa.Column('font_size', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.user_id'], ),
    sa.ForeignKeyConstraint(['user_id2'], ['user_info.user_id'], ),
    sa.PrimaryKeyConstraint('user_id', 'user_id2')
    )
    op.create_table('AI',
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.Column('note_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False, comment='분석 결과'),
    sa.ForeignKeyConstraint(['note_id'], ['notes.note_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.user_id'], ),
    sa.PrimaryKeyConstraint('goal_id')
    )
    op.create_table('api',
    sa.Column('api_id', sa.Integer(), autoincrement=True, nullable=False, comment='자동 생성'),
    sa.Column('note_id', sa.Integer(), nullable=False, comment='자동생성'),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['note_id'], ['notes.note_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.user_id'], ),
    sa.PrimaryKeyConstraint('api_id')
    )
    op.create_table('erd',
    sa.Column('erd_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('note_id', sa.Integer(), nullable=False, comment='자동생성'),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False, comment='자동'),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['note_id'], ['notes.note_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.user_id'], ),
    sa.PrimaryKeyConstraint('erd_id')
    )
    op.drop_table('answer')
    op.drop_table('question')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('subject', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('create_date', mysql.DATETIME(), nullable=False),
    sa.Column('edit_date', mysql.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('answer',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.Column('create_date', mysql.DATETIME(), nullable=False),
    sa.Column('question_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name='answer_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('erd')
    op.drop_table('api')
    op.drop_table('AI')
    op.drop_table('settings')
    op.drop_table('notes')
    op.drop_table('admin_logs')
    op.drop_table('user_info')
    op.drop_table('admin_info')
    # ### end Alembic commands ###