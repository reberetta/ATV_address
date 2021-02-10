'''import pytest
from models.address import Address


class TestAddress:
    def test_address_instance(self):
        description = 'rua amintas'
        number = 453
        cep = '34352-54'
        id_district = 1
        address = Address('rua amintas', number, cep, id_district)
        assert isinstance(address, Address)
        assert address.description == description
        assert address.number == number
        assert address.cep == cep

    def test_address_description_empty(self):
        with pytest.raises(ValueError):
            address = Address('', 453, '34352-54', 1)

    def test_address_description_len(self):
        with pytest.raises(ValueError):
            address = Address('A'*51, 453, '34352-54', 1)

    def test_address_description_int(self):
        with pytest.raises(TypeError):
            address = Address(10, 453, '34352-54', 1)

    #def test_address_number_empty(self):
    #    with pytest.raises(ValueError):
    #        address = Address('rua amintas', None, '34352-54', 1)

    #def test_address_number_str(self):
    #    with pytest.raises(TypeError):
    #        address = Address('rua amintas', '453', '34352-54', 1)

    def test_address_cep_empty(self):
        with pytest.raises(ValueError):
            address = Address('rua amintas', 564, '', 1)

    def test_address_cep_len(self):
        with pytest.raises(ValueError):
            address = Address('rua amintas', 453, '34352-54'*100, 1)

    def test_address_cep_int(self):
        with pytest.raises(TypeError):
            address = Address('rua amintas', 453, 100, 1)

    def test_address_id_district_str(self):
        with pytest.raises(TypeError):
            address = Address('rua amintas', 453, 100, '1')

    def test_address_id_district_lower_than_zero(self):
        with pytest.raises(ValueError):
            address = Address('rua amintas', 453, 100, -5)
'''