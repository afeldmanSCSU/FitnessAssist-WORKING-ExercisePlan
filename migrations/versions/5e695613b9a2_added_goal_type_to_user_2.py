"""Added goal_type to User 2

Revision ID: 5e695613b9a2
Revises: 31263370f4d1
Create Date: 2024-04-07 19:39:09.486645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e695613b9a2'
down_revision = '31263370f4d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('goal_type', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('goal_type')

    # ### end Alembic commands ###
