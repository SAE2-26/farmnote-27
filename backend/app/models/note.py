from datetime import datetime

from sqlalchemy import String, TypeDecorator
from sqlalchemy.engine import Dialect
from sqlmodel import Field, SQLModel


class DateTimeString(TypeDecorator[datetime]):
    impl = String
    cache_ok = True

    def process_bind_param(
        self, value: datetime | None, dialect: Dialect
    ) -> str | None:
        return value.isoformat() if value is not None else None

    def process_result_value(
        self, value: str | None, dialect: Dialect
    ) -> datetime | None:
        return datetime.fromisoformat(value) if value is not None else None


class NoteRecord(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str
    date: datetime | None = Field(default=None, sa_type=DateTimeString)
