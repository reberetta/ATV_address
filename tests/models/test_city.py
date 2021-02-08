import pytest
from models.city import City


class TestCity:
    def test_city_instance():
        city = City('blumenau')
        assert isinstance(city, City)
        assert city.description == 'blumenau'

    def test_city_description_empty():
        with pytest.raises(ValueError):
            city = City('')

    def test_city_description_len():
        with pytest.raises(ValueError):
            city = City('nome aleatorio'*100)

    def test_city_description_int():
        with pytest.raises(TypeError):
            city = City(10)
