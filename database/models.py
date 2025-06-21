from typing import Any

from sqlalchemy.orm import DeclarativeMeta, Mapped, mapped_column, DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    id: Any
    __name__: str

    __allow__unmapped__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class Tasks(Base):
    __tablename__ = "Tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int]

class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[int]
    name: Mapped[str]
