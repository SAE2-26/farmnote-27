from fastapi.testclient import TestClient
from pytest import MonkeyPatch
import pytest


def test_get_notes(client: TestClient):
    notes_response = client.get("/notes")
    assert notes_response.status_code == 200
    assert len(notes_response.json()) == 2


# Monkey patching example
def get_random_value():
    import random
    return random.randint(1, 1000) + 5

def test_get_random_value(monkeypatch: MonkeyPatch):
    random_value = 250
    monkeypatch.setattr("random.randint", lambda a, b: random_value)
    result = get_random_value()
    assert result == random_value + 5

# Parametrized test
@pytest.mark.parametrize("random_value", range(1, 1001))
def test_get_random_value_parametrized(monkeypatch: MonkeyPatch, random_value: int):
    monkeypatch.setattr("random.randint", lambda a, b: random_value)
    result = get_random_value()
    assert result == random_value + 5