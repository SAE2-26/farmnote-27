from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()

class Note(BaseModel):
    title: str
    content: str
    date: datetime | None = None


@app.get("/notes")
def read_notes() -> list[Note]:
    return [
        Note(title="Note 1", content="This is the first note.", date=datetime.now()),
        Note(title="Note 2", content="This is the second note.", date=datetime.now())
    ]

@app.post("/notes")
def create_note(note: Note) -> Note:
    return note