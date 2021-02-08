import pytest
from models.address import Address


class TestAddress:
    def test_address_instance():
        description = 'rua amintas'
        number = 453
        cep = '34352-54'
        address = Address('rua amintas', number, cep)
        assert isinstance(address, Address)
        assert address.description == description
        assert address.number == number
        assert address.cep == cep

    def test_address_description_empty():
        with pytest.raises(ValueError):
            address = Address('', 453, '34352-54')

    def test_address_description_len():
        with pytest.raises(ValueError):
            address = Address('A'*51, 453, '34352-54')

    def test_address_description_int():
        with pytest.raises(TypeError):
            address = Address(10, 453, '34352-54')

    def test_address_number_empty():
        with pytest.raises(ValueError):
            address = Address('rua amintas', None, '34352-54')

    def test_address_number_str():
        with pytest.raises(TypeError):
            address = Address('rua amintas', '453', '34352-54')

    def test_address_cep_empty():
        with pytest.raises(ValueError):
            address = Address('rua amintas', 564, '')

    def test_address_cep_len():
        with pytest.raises(ValueError):
            address = Address('rua amintas', 453, '34352-54'*100)

    def test_address_cep_int():
        with pytest.raises(TypeError):
            address = Address('rua amintas', 453, 100)
