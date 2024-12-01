from typing import Any

from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.gateways.postgresql.models.base import BaseORM, IDMixin


class GeoORM(BaseORM, IDMixin):
    __tablename__ = 'geo'

    name: Mapped[str]
    type: Mapped[str]
    geojson: Mapped[dict[str, Any]] = mapped_column(JSON)
