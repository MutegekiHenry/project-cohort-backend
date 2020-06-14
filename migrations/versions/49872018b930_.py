"""empty message

Revision ID: 49872018b930
Revises: 0263421972ff
Create Date: 2020-06-14 10:42:20.792477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49872018b930'
down_revision = '0263421972ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('business_type', sa.String(length=256), nullable=False),
    sa.Column('age', sa.String(length=256), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('business')
    # ### end Alembic commands ###