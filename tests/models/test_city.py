import pytest
from models.city import City


class TestCity:
    def test_city_instance(self):
        city = City('blumenau')
        assert isinstance(city, City)
        assert city.description == 'blumenau'

    def test_city_description_empty(self):
        with pytest.raises(ValueError):
            city = City('')

    def test_city_description_len(self):
        with pytest.raises(ValueError):
            city = City('nome aleatorio'*100)

    def test_city_description_int(self):
        with pytest.raises(TypeError):
            city = City(10)

    def test_city_id_state_str(self):
        with pytest.raises(TypeError)
            city = City('Blumenau', '1')

    def test_city_id_state_lower_than_zero(self):
        with pytest.raises(ValueError)
            city = City('Blumenau', -5)
