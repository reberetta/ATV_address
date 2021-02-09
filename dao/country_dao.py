import sys
sys.path.append('.')

from dao.base_dao import BaseDao
from models.country import Country


class CountryDao(BaseDao):
    def __init__(self):
        super().__init__(Country)
