from dataclasses import dataclass

from app.domain.entities.geo import GeoEntity
from app.infrastructure.repositories.geo import IGeoRepository
from app.logic.queries.base import IQuery, IQueryUseCase


@dataclass(frozen=True)
class GetGeosQuery(IQuery):
    pass


@dataclass(eq=False, frozen=True)
class GetGeosQueryUseCase(IQueryUseCase[list[GeoEntity]]):
    geo_repository: IGeoRepository

    async def execute(self, query: GetGeosQuery) -> list[GeoEntity]:
        return await self.geo_repository.get_all()
