from dataclasses import dataclass

from app.logic.exceptions.base import ObjectNotFoundException


@dataclass(eq=False, frozen=True)
class GeoNotFoundException(ObjectNotFoundException):
    id: str

    def __str__(self) -> str:
        return f"Geo object with ID<{self.id}> not found"
