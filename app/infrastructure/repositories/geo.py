from abc import ABC
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.geo import GeoEntity
from app.infrastructure.gateways.postgresql.mappers.geo import GeoORMMapper
from app.infrastructure.gateways.postgresql.models import GeoORM


class IGeoRepository(ABC):
    async def create(self, entity: GeoEntity) -> None: ...

    async def get(self, id_: str) -> GeoEntity | None: ...

    async def get_all(self) -> list[GeoEntity]: ...


@dataclass(eq=False, frozen=True)
class SqlAlchemyGeoRepository(IGeoRepository):
    session: AsyncSession

    async def create(self, entity: GeoEntity) -> None:
        db_geo = GeoORMMapper.from_entity(entity)
        self.session.add(db_geo)

    async def get(self, id_: str) -> GeoEntity | None:
        stmt = (
            select(GeoORM)
            .where(GeoORM.id == id_)
        )
        if db_geo := await self.session.scalar(stmt):
            return GeoORMMapper.to_entity(db_geo)

    async def get_all(self) -> list[GeoEntity]:
        stmt = select(GeoORM)
        db_geos = await self.session.scalars(stmt)
        return [GeoORMMapper.to_entity(db_geo) for db_geo in db_geos]