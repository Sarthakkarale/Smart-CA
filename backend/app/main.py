from fastapi import FastAPI

from app.core.config import settings
from app.api.routes.auth_routes import router as auth_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(auth_router)


@app.get("/")
def home():
    return {
        "message": "Smart CA Authentication Backend Running"
    }