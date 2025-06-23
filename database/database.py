from typing import Any

from sqlalchemy.orm import DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id: Any
    __name__: str

    __allow__unmapped__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
