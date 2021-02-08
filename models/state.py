import sys
sys.path.append('.')
from models.base_model import BaseModel
from models.country import Country
from sqlalchemy import Column, String, Integer, ForeingKey, relationship


class State(BaseModel):
    __tablename__ = 'state'
    description = Column(String(length = 50), nullable = False)
    id_country = Column(Integer, ForeingKey( 'country.id' ), nullable = False)
    country = relationship('country')

    def __init__(self, description: str, id_country: int) -> None:
        self.description = description
        self.id_country = id_country
    
    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(description, str, key)
        description = validate_not_empty(description, key)
        return validate_len(description, 50, key)
