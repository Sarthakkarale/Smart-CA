from fastapi import FastAPI

from app.core.config import settings

from app.api.auth.auth_routes import router as auth_router
from app.api.profile.profile_routes import router as profile_router
from app.api.dashboard.dashboard_routes import router as dashboard_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {
        "message": "Smart CA Backend Running"
    }