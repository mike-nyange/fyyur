"""empty message

Revision ID: ee88d76184b6
Revises: 
Create Date: 2022-06-04 15:13:17.804273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee88d76184b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist_genres')
    op.drop_table('venue_genres')
    op.add_column('artists', sa.Column('genres', sa.String(length=200), nullable=True))
    op.add_column('venues', sa.Column('genres', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'genres')
    op.drop_column('artists', 'genres')
    op.create_table('venue_genres',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], name='venue_genres_venue_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='venue_genres_pkey')
    )
    op.create_table('artist_genres',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], name='artist_genres_artist_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='artist_genres_pkey')
    )
    # ### end Alembic commands ###
