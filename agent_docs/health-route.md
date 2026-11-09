# Health route

The backend exposes `GET /health`, returning HTTP 200 and `{"status": "ok"}` when the application is running. The route is covered by a FastAPI test-client test in `backend/tests/routers/test_health.py`.