from src.database import Base
from sqlalchemy import Column, Integer, String, JSON, ForeignKey


class Hotel(Base):
    """Модель отеля"""
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)


class Room(Base):
    """Модель комнаты"""
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, nullable=False)
    hotel_id = Column(ForeignKey("hotel.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
