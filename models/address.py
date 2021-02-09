import sys
sys.path.append('.')
from models.base_model import BaseModel
from models.district import District
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import validates, relationship
from models.district import District
from utils.validators import validate_type, validate_not_empty, validate_len, validate_greater_than_zero


class Address(BaseModel):
    __tablename__ = 'address'
    description = Column(String(length = 50), nullable = False)
    number = Column(Integer, nullable = False)
    cep = Column(String(length = 10), nullable = False)
    id_district = Column(Integer, ForeignKey( 'district.id' ), nullable = False)
    district = relationship('District')

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
        number = validate_type(number, float, key)
        number = validate_not_empty(number, key)
        return validate_be_greater_than_zero(number, key)
    
    @validates('cep')
    def validate_name(self, key, cep):
        cep = validate_not_empty(cep, key)
        cep = validate_type(cep, str, key)
        return validate_len(cep, 10, key)

    @validates('id_district')
    def validate_id_customer(self, key, id_district):
        validate_greater_than_zero(id_district, key)
        return validate_type(id_district, int, key)
