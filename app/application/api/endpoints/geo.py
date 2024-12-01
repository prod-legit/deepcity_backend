from typing import Annotated

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter, Path
from pydantic import UUID4

from app.application.api.schemas.geo import GeoSchema, AddGeoSchema, PatchGeoSchema
from app.logic.commands.geo.add import AddGeoCommandUseCase, AddGeoCommand
from app.logic.commands.geo.patch import PatchGeoCommand, PatchGeoCommandUseCase
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


@router.post(
    path="/",
    operation_id="addGeo",
    summary="Добавить объект",
    response_model=GeoSchema,
    status_code=201
)
async def add_geo(
        data: AddGeoSchema,
        add_geo_use_case: FromDishka[AddGeoCommandUseCase]
) -> GeoSchema:
    geo = await add_geo_use_case.execute(AddGeoCommand(
        name=data.name,
        type=data.type,
        geojson=data.geojson
    ))
    return GeoSchema.from_entity(geo)


@router.patch(
    path="/{geo_id}",
    operation_id="pathGeo",
    summary="Изменить объект",
    response_model=GeoSchema
)
async def patch_geo(
        geo_id: Annotated[UUID4, Path()],
        data: PatchGeoSchema,
        patch_geo_use_case: FromDishka[PatchGeoCommandUseCase]
) -> GeoSchema:
    geo = await patch_geo_use_case.execute(PatchGeoCommand(
        id=geo_id,
        geojson=data.geojson
    ))
    return GeoSchema.from_entity(geo)
