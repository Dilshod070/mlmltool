"""add task table

Revision ID: 9c1ff300fbbc
Revises: 414c3d6039dd
Create Date: 2020-11-13 22:55:01.259591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c1ff300fbbc'
down_revision = '414c3d6039dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('time_created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('complexity', sa.Float(), nullable=True),
    sa.Column('importance', sa.Float(), nullable=True),
    sa.Column('urgency', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['planner_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
