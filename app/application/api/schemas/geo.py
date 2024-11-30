from typing import Any

from pydantic import BaseModel, UUID4

from app.domain.entities.geo import GeoEntity


class GeoSchema(BaseModel):
    id: UUID4
    geojson: dict[str, Any]

    @classmethod
    def from_entity(cls, entity: GeoEntity) -> "GeoSchema":
        return cls(id=entity.id, geojson=entity.geojson)
