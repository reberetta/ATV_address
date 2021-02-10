import sys
sys.path.append('.')

from dao.address_dao import AddressDao
from models.address import Address
import pytest


class TestAddressDao:
    @pytest.fixture
    def create_address(self):
        return Address('Address Test', 200, "79032410", 1)

    @pytest.fixture
    def create_address_dao(self):
        return AddressDao()

    def test_address_dao_instance(self, create_address_dao):
        address_dao = create_address_dao
        assert isinstance(address_dao, AddressDao)

    def test_address_create(self, create_address, create_address_dao):
        address = create_address_dao.save(create_address)
        assert address.id is not None
        create_address_dao.delete(address)

    def test_address_read_by_id(self, create_address, create_address_dao):
        address = create_address_dao.save(create_address)
        address_read = create_address_dao.read_by_id(address.id)
        assert isinstance(address_read, Address)
        assert address.name == address_read.name
        assert address.description == address_read.description
        assert address.price == address_read.price
        create_address_dao.delete(address_read)

    def test_address_read_all(self, create_address_dao):
        address = create_address_dao.read_all()
        assert isinstance(address, list)
        assert all(isinstance(address, Address) for addr in address)

    def test_address_delete(self, create_address, create_address_dao):
        address_save = create_address_dao.save(create_address)
        address = create_address_dao.read_by_id(address_save.id)
        create_address_dao.delete(address)
        address_read = create_address_dao.read_by_id(address_save.id)
        assert address_read is None
