import sys
sys.path.append('.')
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String, Integer, ForeingKey, relationship


class District(BaseModel):
    __tablename__ = 'district'
    description = Column(String(length = 50), nullable = False)
    id_city = Column(Integer, ForeingKey( 'city.id' ), nullable = False)
    city = relationship('city')

    def __init__(self, description: str, id_city: int) -> None:
        self.description = description
        self.id_city = id_city

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(description, str, key)
        description = validate_not_empty(description, key)
        return validate_len(description, 100, key)
