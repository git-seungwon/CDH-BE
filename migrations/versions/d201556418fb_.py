"""empty message

Revision ID: d201556418fb
Revises: 88b13378e536
Create Date: 2024-11-30 13:48:25.278604

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd201556418fb'
down_revision: Union[str, None] = '88b13378e536'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False, comment='PK'),
    sa.Column('invite_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False, comment='사용자 고유 아이디'),
    sa.Column('joined_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['invite_id'], ['group.invite_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_group_invite_id'), 'group', ['invite_id'], unique=True)
    op.drop_constraint('notes_ibfk_2', 'notes', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('notes_ibfk_2', 'notes', 'group', ['teamspace_id'], ['id'])
    op.drop_index(op.f('ix_group_invite_id'), table_name='group')
    op.drop_table('member')
    # ### end Alembic commands ###
