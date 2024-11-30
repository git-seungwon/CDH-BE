"""empty message

Revision ID: e916cf914c03
Revises: 0d4c06237f14
Create Date: 2024-11-30 14:37:51.896065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e916cf914c03'
down_revision: Union[str, None] = '0d4c06237f14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('notes_ibfk_2', table_name='notes')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('notes_ibfk_2', 'notes', ['teamspace_id'], unique=False)
    # ### end Alembic commands ###
