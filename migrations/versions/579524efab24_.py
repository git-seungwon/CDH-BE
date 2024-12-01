"""empty message

Revision ID: 579524efab24
Revises: d5a5364b975d
Create Date: 2024-11-29 12:02:00.919766

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '579524efab24'
down_revision: Union[str, None] = 'd5a5364b975d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_group_invite_id'), 'group', ['invite_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_group_invite_id'), table_name='group')
    # ### end Alembic commands ###