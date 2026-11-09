from datetime import datetime

from fastapi import APIRouter

from app.schemas.note import Note

router = APIRouter()


@router.get("/notes")
def read_notes() -> list[Note]:
    return [
        Note(title="Note 1", content="This is the first note.", date=datetime.now()),
        Note(title="Note 2", content="This is the second note.", date=datetime.now()),
    ]


@router.post("/notes")
def create_note(note: Note) -> Note:
    return note
