from fastapi.testclient import TestClient


def test_get_notes(client: TestClient):
    notes_response = client.get("/notes")
    assert notes_response.status_code == 200
    assert notes_response.json() == []


def test_note_crud(client: TestClient):
    note = {"title": "Field", "content": "Check soil", "date": "2026-11-09T12:00:00"}
    response = client.post("/notes", json=note)
    assert response.status_code == 201
    created = response.json()
    assert created == {"id": created["id"], **note}

    note_url = f"/notes/{created['id']}"
    assert client.get(note_url).json() == created
    assert client.get("/notes").json() == [created]

    updated = {"title": "Field updated", "content": "Plant seeds", "date": None}
    response = client.put(note_url, json=updated)
    assert response.status_code == 200
    assert response.json() == {"id": created["id"], **updated}
    assert client.get(note_url).json() == response.json()

    assert client.delete(note_url).status_code == 204
    assert client.get("/notes").json() == []
    assert client.get(note_url).status_code == 404
    assert client.put(note_url, json=updated).status_code == 404
    assert client.delete(note_url).status_code == 404


def test_note_timezone_and_validation(client: TestClient):
    note = {
        "title": "Field",
        "content": "Check soil",
        "date": "2026-11-09T12:00:00+02:00",
    }
    created = client.post("/notes", json=note).json()
    assert client.get(f"/notes/{created['id']}").json()["date"] == note["date"]
    assert client.post("/notes", json={"title": "Missing content"}).status_code == 422
    assert client.post("/notes", json={**note, "date": "not a date"}).status_code == 422
