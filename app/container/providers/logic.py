from dishka import Provider, provide, Scope

from app.logic.queries.geo.get import GetGeoQueryUseCase
from app.logic.queries.geo.get_all import GetGeosQueryUseCase


class LogicProvider(Provider):
    get_geo_query_use_case = provide(GetGeoQueryUseCase, scope=Scope.REQUEST)
    get_geos_query_use_case = provide(GetGeosQueryUseCase, scope=Scope.REQUEST)
