from dishka import Provider, provide, Scope

from app.infrastructure.repositories.geo import IGeoRepository, SqlAlchemyGeoRepository


class InfrastructureProvider(Provider):
    geo_repository = provide(
        SqlAlchemyGeoRepository,
        scope=Scope.REQUEST,
        provides=IGeoRepository
    )
