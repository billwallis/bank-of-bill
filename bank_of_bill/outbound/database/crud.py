import abc
from typing import Protocol, TypeVar

Resource = TypeVar("Resource")
CreationData = TypeVar("CreationData")
Identifier = TypeVar("Identifier")


class CRUDInterface(abc.ABC):
    @abc.abstractmethod
    def create(self, data: CreationData) -> Resource:
        pass

    @abc.abstractmethod
    def read(self, id_: Identifier) -> Resource:
        pass

    @abc.abstractmethod
    def update(self, resource: Resource) -> None:
        pass

    @abc.abstractmethod
    def delete(self, id_: Identifier) -> None:
        pass


# class CRUDInterface(Protocol[Resource, CreationData, Identifier]):
#     def create(self, data: CreationData) -> Resource:
#         pass
#
#     def read(self, id_: Identifier) -> Resource:
#         pass
#
#     def update(self, resource: Resource) -> None:
#         pass
#
#     def delete(self, id_: Identifier) -> None:
#         pass


class DatabaseConnection(Protocol):
    def commit(self) -> None:
        pass

    def rollback(self) -> None:
        pass


class DatabaseCursor(Protocol):
    def execute(self, *args, **kwargs) -> None:
        pass

    def fetchone(self, *args, **kwargs) -> tuple:
        pass
