"""empty message

Revision ID: 4832a8fe3a49
Revises: 
Create Date: 2021-09-09 11:15:25.433641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4832a8fe3a49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('pwd', sa.String(length=20), nullable=False),
    sa.Column('tel', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prod_cate',
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('num')
    )
    op.create_table('board',
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('writer', sa.String(length=20), nullable=True),
    sa.Column('w_date', sa.DateTime(), nullable=False),
    sa.Column('loc', sa.String(length=50), nullable=False),
    sa.Column('p_cate_num', sa.Integer(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('content', sa.String(length=200), nullable=False),
    sa.Column('img1', sa.String(length=100), nullable=True),
    sa.Column('img2', sa.String(length=100), nullable=True),
    sa.Column('img3', sa.String(length=100), nullable=True),
    sa.Column('cnt', sa.Integer(), nullable=False),
    sa.Column('like', sa.Integer(), nullable=False),
    sa.Column('state', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['p_cate_num'], ['prod_cate.num'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['writer'], ['member.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('num')
    )
    op.create_table('msg',
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('b_num', sa.Integer(), nullable=True),
    sa.Column('like_id', sa.String(length=20), nullable=True),
    sa.Column('tel', sa.String(length=20), nullable=False),
    sa.Column('content', sa.String(length=100), nullable=True),
    sa.Column('checked', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['b_num'], ['board.num'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['like_id'], ['member.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('num')
    )
    op.create_table('prod_like',
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('id', sa.String(length=20), nullable=True),
    sa.Column('b_num', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['b_num'], ['board.num'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id'], ['member.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prod_like')
    op.drop_table('msg')
    op.drop_table('board')
    op.drop_table('prod_cate')
    op.drop_table('member')
    # ### end Alembic commands ###
