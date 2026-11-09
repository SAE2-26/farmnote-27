from datetime import datetime

from pydantic import BaseModel


class Note(BaseModel):
    title: str
    content: str
    date: datetime | None = None


class NoteRead(Note):
    id: int
