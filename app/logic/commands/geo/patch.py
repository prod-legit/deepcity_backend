from dataclasses import dataclass
from typing import Any

from app.domain.entities.geo import GeoEntity
from app.infrastructure.repositories.geo import IGeoRepository
from app.logic.commands.base import ICommand, ICommandUseCase
from app.logic.exceptions.geo import GeoNotFoundException


@dataclass(frozen=True)
class PatchGeoCommand(ICommand):
    id: str
    geojson: dict[str, Any]


@dataclass(eq=False, frozen=True)
class PatchGeoCommandUseCase(ICommandUseCase[GeoEntity]):
    geo_repository: IGeoRepository

    async def execute(self, command: PatchGeoCommand) -> GeoEntity:
        geo = await self.geo_repository.get(command.id)
        if geo is None:
            raise GeoNotFoundException(command.id)

        geo.geojson = command.geojson
        await self.geo_repository.update(geo)

        return geo
