from fastapi import APIRouter
from sqlalchemy import select
from src.bookings.models import Booking
from src.database import async_session_maker


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Booking)
        result = await session.execute(query)
        return result.scalars().all()



