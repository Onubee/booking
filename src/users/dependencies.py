from datetime import datetime, timezone

from fastapi import Request, Depends
from jose import JWTError, jwt

from src.config import settings
from src.exceptions import UserNotExistsException
from src.users.service import UserService


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise UserNotExistsException()
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except JWTError:
        raise UserNotExistsException()
    expire: str = payload.get("exp")
    if not expire or int(expire) < datetime.now(timezone.utc).timestamp():
        raise UserNotExistsException()
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserNotExistsException()
    user = await UserService.find_by_id(int(user_id))
    if not user:
        raise UserNotExistsException()
    return user
