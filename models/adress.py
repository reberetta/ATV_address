import sys
sys.path.append('.')
from models.base_model import BaseModel
from models.district import District
from sqlalchemy import Column, String, Integer, ForeingKey, relationship


class Adress(BaseModel):
    __tablename__ = 'adress'
    description = Column(String(length = 50), nullable = False)
    number = Column(Integer, nullable = False)
    cep = Column(String(length = 10), nullable = False)
    id_district = Column(Integer, ForeingKey( 'district.id' ), nullable = False)
    district = relationship('district')

    def __init__(self, description: str, number: int, cep: str, id_district: int) -> None:
        self.description = description
        self.number = number
        self.cep = cep
        self.id_district = id_district

    @validates('description')
    def validate_description(self, key, description):
        description = validate_not_empty(description, key)
        description = validate_type(description, str, key)
        return validate_len(description, 50, key)

    @validates('number')
    def validate_number(self, key, number):
        number = validate_not_empty(number, key)
        number = validate_type(number, float, key)
        return validate_be_greater_than_zero(number, key)
    
    @validates('cep')
    def validate_name(self, key, cep):
        cep = validate_not_empty(cep, key)
        cep = validate_type(cep, str, key)
        return validate_len(cep, 10, key)
