"""geo

Revision ID: df6c8e77a293
Revises: 
Create Date: 2024-11-30 13:59:52.613388

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "df6c8e77a293"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "geo",
        sa.Column("id", sa.UUID(as_uuid=False), nullable=False),
        sa.Column("geojson", postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_geo")),
        sa.UniqueConstraint("id", name=op.f("uq_geo_id"))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("geo")
    # ### end Alembic commands ###
