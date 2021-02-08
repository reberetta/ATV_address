from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeingKey, relationship


class Country(BaseModel):
    __tablename__ = 'country'
    description = Column(String(length = 50), nullable = False)

    def __init__(self, description: str) -> None:
        self.description = description
