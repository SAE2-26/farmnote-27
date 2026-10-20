from fastapi.testclient import TestClient


def test_get_notes(client: TestClient):
    notes_response = client.get("/notes")
    assert notes_response.status_code == 200
    assert len(notes_response.json()) == 2