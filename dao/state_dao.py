import sys
sys.path.append('.')

from dao.base_dao import BaseDao
from models.state import State


class StateDao(BaseDao):
    def __init__(self):
        super().__init__(State)
