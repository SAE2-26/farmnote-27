from random import choice

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


# Test Driven Development (TDD) example
def generate_random_token():
    special_characters = "!@#$%^&*()-+"
    
    token = "M"
    token += str(choice("0123456789"))
    token += str(choice("abcdefghijklmnopqrstuvwxyz"))
    for _ in range(3):
        token += choice(special_characters)
    return token

def test_returns_string():
    result = generate_random_token()
    assert isinstance(result, str)

def test_returns_six_characters():
    result = generate_random_token()
    assert len(result) == 6

def test_returns_at_least_one_uppercase_lowercase_digit_and_special_character():
    result = generate_random_token()
    assert any(c.isupper() for c in result)
    assert any(c.islower() for c in result)
    assert any(c.isdigit() for c in result)
    assert any(c in "!@#$%^&*()-+" for c in result)

def test_first_character_is_M():
    result = generate_random_token()
    assert result[0].lower() == "m"

def test_no_duplicate_characters_and_random():
    result = generate_random_token()
    assert len(result) == len(set(result))
    result2 = generate_random_token()
    assert result != result2