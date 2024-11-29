from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from app.application.api.schemas.status import StatusSchema

router = APIRouter(
    prefix="/ping",
    tags=["Ping"],
    route_class=DishkaRoute
)


@router.get(
    path="/",
    summary="Пинг",
    operation_id="ping",
    status_code=200,
    response_model=StatusSchema
)
async def register_user() -> StatusSchema:
    return StatusSchema(status=True, message="Pong")
