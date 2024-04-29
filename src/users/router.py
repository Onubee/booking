from fastapi import APIRouter, Response, Depends

from src.exceptions import UserAlreadyExistsException, UserNotExistsException
from src.users.auth import get_password_hash, authenticate_user, create_access_token
from src.users.dependencies import get_current_user
from src.users.models import User
from src.users.schemas import SUserAuth
from src.users.service import UserService


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistsException()
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise UserNotExistsException()
    access_token = create_access_token(data={"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return f"Вы успешно вышли"


@router.get("/me")
async def read_me(current_user: User = Depends(get_current_user)):
    return current_user
