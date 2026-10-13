from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()

class Note(BaseModel):
    title: str
    content: str
    date: datetime


@app.get("/notes")
def read_notes() -> list[Note]:
    return [
        Note(title="Note 1", content="This is the first note.", date=datetime.now()),
        Note(title="Note 2", content="This is the second note.", date=datetime.now())
    ]