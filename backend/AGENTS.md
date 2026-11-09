# Commands
```
uv run fastapi dev: Run dev backend
pytest: Run python tests
ruff: Run linter, prettifier and checks
```

# Project Structure
```
.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   ├── config.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── schemas
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── user.py
│   └── models
│   │   ├── __init__.py
│   │   ├── item.py
│   │   └── user.py
│   └── internal
│       ├── __init__.py
│       └── admin.py
```

# Rules
* Before you commit, run `pytest`, `ruff check`, and `ruff format --check`.
* For tests, mirror the file structure of the `app` folder.

# Tech-Stack
* sqlmodel: ORM library
* sqlite: db in the local filesystem