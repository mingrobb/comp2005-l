"""Added Comments Model

Revision ID: f8d881d25005
Revises: 3452ed51b565
Create Date: 2018-04-01 15:53:10.549397

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f8d881d25005'
down_revision = '3452ed51b565'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('body', sa.String(length=255), nullable=False),
                    sa.Column('poster_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
                    sa.ForeignKeyConstraint(['poster_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###