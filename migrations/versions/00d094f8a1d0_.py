"""empty message

Revision ID: 00d094f8a1d0
Revises: 49872018b930
Create Date: 2020-06-14 11:03:30.507791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00d094f8a1d0'
down_revision = '49872018b930'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('gender', sa.String(length=256), nullable=False),
    sa.Column('address', sa.String(length=256), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###