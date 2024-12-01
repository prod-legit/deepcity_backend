from dataclasses import dataclass
from typing import Any

from app.domain.entities.geo import GeoEntity
from app.infrastructure.repositories.geo import IGeoRepository
from app.logic.commands.base import ICommand, ICommandUseCase
from app.logic.exceptions.geo import GeoExistsException


@dataclass(frozen=True)
class AddGeoCommand(ICommand):
    name: str
    type: str
    geojson: dict[str, Any]


@dataclass(eq=False, frozen=True)
class AddGeoCommandUseCase(ICommandUseCase[GeoEntity]):
    geo_repository: IGeoRepository

    async def execute(self, command: AddGeoCommand) -> GeoEntity:
        if await self.geo_repository.name_exists(command.name):
            raise GeoExistsException(command.name)

        geo = GeoEntity(
            name=command.name,
            type=command.type,
            geojson=command.geojson
        )
        await self.geo_repository.create(geo)

        return geo
