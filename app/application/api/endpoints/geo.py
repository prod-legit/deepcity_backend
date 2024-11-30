from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Path
from pydantic import UUID4

from app.application.api.schemas.geo import GeoSchema
from app.logic.queries.geo.get import GetGeoQueryUseCase, GetGeoQuery
from app.logic.queries.geo.get_all import GetGeosQueryUseCase, GetGeosQuery

router = APIRouter(
    prefix="/geo",
    tags=["Geo"],
    route_class=DishkaRoute
)


@router.get(
    path="/{geo_id}",
    operation_id="getGeo",
    summary="Получить объект",
    response_model=GeoSchema
)
async def get_geo(
        geo_id: Annotated[UUID4, Path()],
        get_geo_use_case: FromDishka[GetGeoQueryUseCase]
) -> GeoSchema:
    geo = await get_geo_use_case.execute(GetGeoQuery(geo_id))
    return GeoSchema.from_entity(geo)


@router.get(
    path="/",
    operation_id="getGeos",
    summary="Получить все объекты",
    response_model=list[GeoSchema]
)
async def get_geos(get_geos_use_case: FromDishka[GetGeosQueryUseCase]) -> list[GeoSchema]:
    geos = await get_geos_use_case.execute(GetGeosQuery())
    return [GeoSchema.from_entity(geo) for geo in geos]
