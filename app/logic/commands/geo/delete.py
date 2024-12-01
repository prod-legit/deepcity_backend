from dataclasses import dataclass

from app.infrastructure.repositories.geo import IGeoRepository
from app.logic.commands.base import ICommand, ICommandUseCase
from app.logic.exceptions.geo import GeoNotFoundException


@dataclass(frozen=True)
class DeleteGeoCommand(ICommand):
    id: str


@dataclass(eq=False, frozen=True)
class DeleteGeoCommandUseCase(ICommandUseCase[None]):
    geo_repository: IGeoRepository

    async def execute(self, command: DeleteGeoCommand) -> None:
        geo = await self.geo_repository.get(command.id)
        if geo is None:
            raise GeoNotFoundException(command.id)

        await self.geo_repository.delete(command.id)
