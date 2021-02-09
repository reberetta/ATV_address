import sys
sys.path.append('.')

from dao.base_dao import BaseDao
from models.address import Address


class AddressDao(BaseDao):
    def __init__(self):
        super().__init__(Address)

add = AddressDao().save(Address("Rua oi", 3, "5678", 1))
print(add.id_)