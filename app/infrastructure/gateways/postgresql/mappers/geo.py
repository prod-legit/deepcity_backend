from app.domain.entities.geo import GeoEntity
from app.infrastructure.gateways.postgresql.mappers.base import IORMMapper
from app.infrastructure.gateways.postgresql.models import GeoORM


class GeoORMMapper(IORMMapper[GeoEntity, GeoORM]):
    @staticmethod
    def from_entity(entity: GeoEntity) -> GeoORM:
        return GeoORM(
            id=entity.id,
            geojson=entity.geojson
        )

    @staticmethod
    def to_entity(orm: GeoORM) -> GeoEntity:
        return GeoEntity(
            id=orm.id,
            geojson=orm.geojson
        )
