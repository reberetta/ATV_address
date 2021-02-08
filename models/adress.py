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
