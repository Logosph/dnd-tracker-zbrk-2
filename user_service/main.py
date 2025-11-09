from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.config.settings import settings
import uvicorn

from app.db.db_vitals import create_tables
from app.routes.user_routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.db.models.user import User
    await create_tables()
    yield
app = FastAPI(title="Auth Service", root_path=f"/api/v1/auth", lifespan=lifespan)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_CREDENTIALS,
    allow_methods=settings.CORS_METHODS,
    allow_headers=settings.CORS_HEADERS,
)
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Auth Service is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)