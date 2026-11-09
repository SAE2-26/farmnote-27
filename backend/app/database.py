from collections.abc import Iterator
from pathlib import Path

from sqlmodel import Session, SQLModel, create_engine

database_path = Path(__file__).resolve().parent.parent / "farmnote.db"
engine = create_engine(
    f"sqlite:///{database_path}", connect_args={"check_same_thread": False}
)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
