import pytest
from models.country import Country


class TestCountry:
    def test_country_instance():
        country = Country('brasil')
        assert isinstance(country, Country)
        assert country.description == 'brasil'

    def test_country_description_empty():
        with pytest.raises(ValueError):
            country = Country('')

    def test_country_description_len():
        with pytest.raises(ValueError):
            country = Country('nome aleatorio'*100)

    def test_country_description_int():
        with pytest.raises(TypeError):
            country = Country(10)
