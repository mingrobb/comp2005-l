"""Added DirectMessaging

Revision ID: ca049c721f72
Revises: f8d881d25005
Create Date: 2018-04-01 16:43:17.212072

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ca049c721f72'
down_revision = 'f8d881d25005'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('direct_messaging',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('body', sa.String(length=255), nullable=False),
                    sa.Column('sender_id', sa.Integer(), nullable=False),
                    sa.Column('recipient_id', sa.Integer(), nullable=False),
                    sa.Column('date', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], ),
                    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('direct_messaging')
    # ### end Alembic commands ###