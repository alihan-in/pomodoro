from fastapi import APIRouter
from settings import Settings

router = APIRouter(prefix="/ping", tags=["ping"])


@router.get("/db")
async def ping_db():
    settings = Settings()
    return {"message": settings.GOOGLE_TOKEN_ID}

@router.get("/api")
async def ping_app():
    return {"text": "app_is_working"}