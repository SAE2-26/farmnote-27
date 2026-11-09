from fastapi.testclient import TestClient
from pytest import MonkeyPatch
from sqlmodel import create_engine

from app.main import app


def test_notes_persist_after_restart(tmp_path, monkeypatch: MonkeyPatch):
    engine = create_engine(
        f"sqlite:///{tmp_path / 'notes.db'}", connect_args={"check_same_thread": False}
    )
    monkeypatch.setattr("app.database.engine", engine)
    try:
        with TestClient(app) as first_client:
            response = first_client.post(
                "/notes", json={"title": "Field", "content": "Check soil"}
            )
            assert response.status_code == 201
            created = response.json()
        with TestClient(app) as second_client:
            assert second_client.get(f"/notes/{created['id']}").json() == created
    finally:
        engine.dispose()
