# Note CRUD

The notes API stores records in `backend/farmnote.db` using SQLModel and SQLite. The database and tables are created when the FastAPI application starts. Tests in `backend/tests/routers/test_notes.py` override the database session with an isolated in-memory database; `backend/tests/test_database.py` verifies file persistence across application restarts.

- `GET /notes`: list notes.
- `POST /notes`: create a note, returning HTTP 201 and the stored note.
- `GET /notes/{note_id}`: retrieve a note.
- `PUT /notes/{note_id}`: replace the title, content, and optional date.
- `DELETE /notes/{note_id}`: delete a note, returning HTTP 204.

Requests use `title` and `content` strings and an optional ISO 8601 `date`. Responses also include an integer `id`. Missing IDs return HTTP 404. Date values are stored as ISO 8601 strings to preserve timezone offsets and support existing timezone-free values.