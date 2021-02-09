import sys
sys.path.append('.')

from dao.base_dao import BaseDao
from models.city import City


class CityDao(BaseDao):
    def __init__(self):
        super().__init__(City)
