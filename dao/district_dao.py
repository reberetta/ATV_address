import sys
sys.path.append('.')

from dao.base_dao import BaseDao
from models.district import District


class DistrictDao(BaseDao):
    def __init__(self):
        super().__init__(District)
