import sys
sys.path.append('.')
from models.base_model import BaseModel
from models.state import State
from sqlalchemy import Column, String, Integer, ForeingKey, relationship


class City(BaseModel):
    __tablename__ = 'city'
    description = Column(String(length = 50), nullable = False)
    id_state = Column(Integer, ForeingKey( 'state.id' ), nullable = False)
    state = relationship('state')

    def __init__(self, description: str, id_state: int) -> None:
        self.description = description
        self.id_state = id_state
