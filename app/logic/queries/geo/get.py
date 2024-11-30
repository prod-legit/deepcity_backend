from dataclasses import dataclass

from app.domain.entities.geo import GeoEntity
from app.infrastructure.repositories.geo import IGeoRepository
from app.logic.exceptions.geo import GeoNotFoundException
from app.logic.queries.base import IQuery, IQueryUseCase


@dataclass(frozen=True)
class GetGeoQuery(IQuery):
    id: str


@dataclass(eq=False, frozen=True)
class GetGeoQueryUseCase(IQueryUseCase[GeoEntity]):
    geo_repository: IGeoRepository

    async def execute(self, query: GetGeoQuery) -> GeoEntity:
        geo = await self.geo_repository.get(query.id)
        if geo is None:
            raise GeoNotFoundException(query.id)

        return geo
