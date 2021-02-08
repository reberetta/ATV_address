import pytest
from models.district import District


class TestDistrict:
    def test_district_instance():
        district = District('centro')
        assert isinstance(district, District)
        assert district.description == 'centro'

    def test_district_description_empty():
        with pytest.raises(ValueError):
            district = District('')

    def test_district_description_len():
        with pytest.raises(ValueError):
            district = District('nome aleatorio'*100)

    def test_district_description_int():
        with pytest.raises(TypeError):
            district = District(10)
