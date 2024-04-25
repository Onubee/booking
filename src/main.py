from datetime import date

from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel

app = FastAPI()


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


@app.get("/hotels/")
async def say_hello(search_params: HotelsSearchParams = Depends()):
    return search_params


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass
