"""Favorite

Revision ID: d2424d710000
Revises: 7998b8e85812
Create Date: 2025-01-20 11:12:08.769112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2424d710000'
down_revision = '7998b8e85812'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('original_name', sa.String(length=100), nullable=True),
    sa.Column('original_lat', sa.Float(), nullable=False),
    sa.Column('original_lon', sa.Float(), nullable=False),
    sa.Column('antipode_name', sa.String(length=100), nullable=True),
    sa.Column('antipode_lat', sa.Float(), nullable=False),
    sa.Column('antipode_lon', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    # ### end Alembic commands ###
