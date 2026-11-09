# Backend structure

The FastAPI application is composed in `backend/app/main.py`. Route handlers are grouped under `backend/app/routers`, response/request models under `backend/app/schemas`, and shared application configuration under `backend/app/config.py`. Existing routes and their HTTP contracts are unchanged.

Only modules needed by the current health and notes endpoints are present. Add dependencies, persistence models, or additional domain modules when corresponding behavior is introduced.