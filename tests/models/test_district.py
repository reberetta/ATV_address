import pytest
from models.district import District


class TestDistrict:
    def test_district_instance(self):
        district = District('centro')
        assert isinstance(district, District)
        assert district.description == 'centro'

    def test_district_description_empty(self):
        with pytest.raises(ValueError):
            district = District('')

    def test_district_description_len(self):
        with pytest.raises(ValueError):
            district = District('nome aleatorio'*100)

    def test_district_description_int(self):
        with pytest.raises(TypeError):
            district = District(10)

    def test_district_id_city_str(self):
        with pytest.raises(TypeError)
            district = District('centro', '1')

    def test_district_id_city_lower_than_zero(self):
        with pytest.raises(ValueError)
            district = District('centro', -5)
