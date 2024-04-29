from sqlalchemy import Column, Integer, String
from src.database import Base


class User(Base):
    """Модель пользователя"""
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    