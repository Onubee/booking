from fastapi import APIRouter


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@router.get("")
async def get_bookings():
    pass


@router.get("/{booking_id}")
async def get_bookings(booking_id):
    pass

