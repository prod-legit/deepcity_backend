from dataclasses import dataclass

from app.logic.exceptions.base import ObjectNotFoundException, ObjectExistsException


@dataclass(eq=False, frozen=True)
class GeoNotFoundException(ObjectNotFoundException):
    id: str

    def __str__(self) -> str:
        return f"Geo object with ID<{self.id}> not found"


@dataclass(eq=False, frozen=True)
class GeoExistsException(ObjectExistsException):
    name: str

    def __str__(self) -> str:
        return f"Geo object with name<{self.name}> exists"
