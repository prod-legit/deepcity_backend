from dataclasses import dataclass
from typing import Any

from app.domain.entities.base import BaseEntity, IDMixin


@dataclass
class GeoEntity(BaseEntity, IDMixin):
    geojson: dict[str, Any]
