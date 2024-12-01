from typing import Self, Any

from pydantic import BaseModel, UUID4

from app.domain.entities.geo import GeoEntity


class GeoSchema(BaseModel):
    id: UUID4
    name: str
    type: str
    geojson: dict[str, Any]

    @classmethod
    def from_entity(cls, entity: GeoEntity) -> Self:
        return cls(
            id=entity.id,
            name=entity.name,
            type=entity.type,
            geojson=entity.geojson
        )


class AddGeoSchema(BaseModel):
    name: str
    type: str
    geojson: dict[str, Any]


class PatchGeoSchema(BaseModel):
    geojson: dict[str, Any]
