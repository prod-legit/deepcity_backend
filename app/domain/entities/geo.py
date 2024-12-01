from dataclasses import dataclass
from typing import Any

from app.domain.entities.base import BaseEntity, IDMixin


@dataclass
class GeoEntity(BaseEntity, IDMixin):
    name: str
    type: str
    geojson: dict[str, Any]
