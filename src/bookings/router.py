from fastapi import APIRouter

from src.bookings.service import BookingService
from src.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    """Получение все отелей"""
    return await BookingService.find_all()
