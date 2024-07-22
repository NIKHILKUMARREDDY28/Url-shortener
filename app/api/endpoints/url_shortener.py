from fastapi import APIRouter
from pydantic import BaseModel

from app.utils.shortenurl import generate_short_url_for_user

url_shortener_router = APIRouter()


class ShortenerPayload(BaseModel):
    long_url: str
    user_id: str

shortend_url_domain = "https://weshorturl.app/"

@url_shortener_router.post("/shorten")
async def shorten_url(request_data: ShortenerPayload):
    try:
        shortened_url = generate_short_url_for_user(request_data.long_url, request_data.user_id)
    except ValueError as e:
        return {"error": str(e)}
    else:
        return {"shortened_url": shortend_url_domain + shortened_url}
