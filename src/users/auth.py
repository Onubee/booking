from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from src.config import settings
from src.users.service import UserService


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    """Получение хеш-пароля"""
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    """Проврка совпадения пароля"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    """Создание jwt токена"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    """Аутентификация пользователя"""
    user = await UserService.find_one_or_none(email=email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
