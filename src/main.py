from datetime import date
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

from src.bookings.router import router as bookings_router
from src.users.router import router as users_router

app = FastAPI()

app.include_router(bookings_router)
app.include_router(users_router)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


class HotelsSearchParams:
    def __init__(
            self,
            location: str,
            date_from: date,
            date_to: date,
            has_spa: bool | None = None,
            stars: int | None = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get("/hotels")
async def say_hello(search_params: HotelsSearchParams = Depends()):
    return search_params
