"""update database with column information

Revision ID: 0dc704b8c559
Revises: a07ea2734aaa
Create Date: 2023-11-26 15:57:02.759254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0dc704b8c559'
down_revision = 'a07ea2734aaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo_list', schema=None) as batch_op:
        batch_op.add_column(sa.Column('information', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo_list', schema=None) as batch_op:
        batch_op.drop_column('information')

    # ### end Alembic commands ###
