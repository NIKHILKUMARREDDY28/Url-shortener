from fastapi import APIRouter
from app.api.endpoints import url_shortener

internal_router = APIRouter()

internal_router.include_router(url_shortener.url_shortener_router, prefix="/url_shortener")


