import pytest
from models.address import Address


class TestState:
    def test_address_instance():
        address = State('rua amintas', 453, '34352-54')
        assert isinstance(address, State)
        assert address.description == 'rua amintas'
        assert address.number == 453
        assert address.cep == '34352-54'

    def test_address_name_empty():
        with pytest.raises(ValueError):
            address = State('')

    def test_address_name_len():
        with pytest.raises(ValueError):
            address = Address('rua amintas'*100, 453, '34352-54')

    def test_address_name_int():
        with pytest.raises(TypeError):
            address = Address(10)

    def test_address_number_empty():
        with pytest.raises(ValueError):
            address = Address('rua amintas', None, '34352-54')

    def test_address_number_str():
        with pytest.raises(TypeError):
            address = Address('rua amintas', '453', '34352-54')

    def test_address_description_empty():
        with pytest.raises(ValueError):
            address = Address('rua amintas', 564, '')

    def test_address_description_len():
        with pytest.raises(ValueError):
            address = Address('rua amintas', 453, '34352-54'*100)

    def test_address_description_int():
        with pytest.raises(TypeError):
            address = Address('rua amintas', 453, 100)
