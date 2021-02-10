import sys
sys.path.append('.')
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import validates, relationship
from models.state import State
from utils.validators import validate_type, validate_not_empty, validate_len, validate_greater_than_zero


class City(BaseModel):
    __tablename__ = 'city'
    description = Column(String(length = 50), nullable = False)
    id_state = Column(Integer, ForeignKey( 'state.id' ), nullable = False)
    state = relationship('State')

    def __init__(self, description: str, id_state: int) -> None:
        self.description = description
        self.id_state = id_state

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(description, str, key)
        description = validate_not_empty(description, key)
        return validate_len(description, 50, key)

    @validates('id_state')
    def validate_id_customer(self, key, id_state):
        validate_greater_than_zero(id_state, key)
        return validate_type(id_state, int, key)
