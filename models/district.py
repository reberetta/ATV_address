import sys
sys.path.append('.')
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import validates, relationship
from models.city import City
from utils.validators import validate_type, validate_not_empty, validate_len, validate_greater_than_zero


class District(BaseModel):
    __tablename__ = 'district'
    description = Column(String(length = 50), nullable = False)
    id_city = Column(Integer, ForeignKey( 'city.id' ), nullable = False)
    city = relationship('City')

    def __init__(self, description: str, id_city: int) -> None:
        self.description = description
        self.id_city = id_city

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(description, str, key)
        description = validate_not_empty(description, key)
        return validate_len(description, 50, key)

    @validates('id_city')
    def validate_id_customer(self, key, id_city):
        validate_greater_than_zero(id_city, key)
        return validate_type(id_city, int, key)
