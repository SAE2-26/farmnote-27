from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlmodel import Session, select

from app.database import get_session
from app.models.note import NoteRecord
from app.schemas.note import Note, NoteRead

router = APIRouter()
SessionDep = Annotated[Session, Depends(get_session)]


@router.get("/notes", response_model=list[NoteRead])
def read_notes(session: SessionDep) -> list[NoteRecord]:
    return list(session.exec(select(NoteRecord)).all())


@router.post("/notes", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(note: Note, session: SessionDep) -> NoteRecord:
    record = NoteRecord.model_validate(note)
    session.add(record)
    session.commit()
    session.refresh(record)
    return record


def get_note_or_404(note_id: int, session: Session) -> NoteRecord:
    note = session.get(NoteRecord, note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.get("/notes/{note_id}", response_model=NoteRead)
def read_note(note_id: int, session: SessionDep) -> NoteRecord:
    return get_note_or_404(note_id, session)


@router.put("/notes/{note_id}", response_model=NoteRead)
def update_note(note_id: int, note: Note, session: SessionDep) -> NoteRecord:
    record = get_note_or_404(note_id, session)
    record.sqlmodel_update(note.model_dump())
    session.add(record)
    session.commit()
    session.refresh(record)
    return record


@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, session: SessionDep) -> Response:
    record = get_note_or_404(note_id, session)
    session.delete(record)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
