from dishka import Provider, provide, Scope

from app.logic.commands.geo.add import AddGeoCommandUseCase
from app.logic.commands.geo.delete import DeleteGeoCommandUseCase
from app.logic.commands.geo.patch import PatchGeoCommandUseCase
from app.logic.queries.geo.get import GetGeoQueryUseCase
from app.logic.queries.geo.get_all import GetGeosQueryUseCase


class LogicProvider(Provider):
    get_geo_query_use_case = provide(GetGeoQueryUseCase, scope=Scope.REQUEST)
    get_geos_query_use_case = provide(GetGeosQueryUseCase, scope=Scope.REQUEST)
    add_geo_command_use_case = provide(AddGeoCommandUseCase, scope=Scope.REQUEST)
    patch_geo_command_use_case = provide(PatchGeoCommandUseCase, scope=Scope.REQUEST)
    delete_geo_command_use_case = provide(DeleteGeoCommandUseCase, scope=Scope.REQUEST)
