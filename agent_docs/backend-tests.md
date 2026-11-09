# Backend tests

Backend application tests mirror `backend/app`: router tests live in `backend/tests/routers`, and database persistence tests live in `backend/tests/test_database.py`. The shared client fixture in `backend/tests/conftest.py` uses an isolated in-memory database. Existing standalone testing examples remain in `backend/tests/test_main.py`.