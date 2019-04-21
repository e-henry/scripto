"""Add periodicity of script

Revision ID: 147d1de2e5e4
Revises: 
Create Date: 2019-04-19 18:48:33.526449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '147d1de2e5e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('script', sa.Column('periodicity', sa.String(),server_default='daily'))


def downgrade():
    # Sqlite does not handle the drop column directive, but alembic can take care of
    # creating a migration script if we use its batch mode
    with op.batch_alter_table("script") as batch_op:
        batch_op.drop_column('periodicity')
