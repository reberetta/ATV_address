'''import pytest
from models.state import State


class TestState:
    def test_state_instance(self):
        state = State('parana')
        assert isinstance(state, State)
        assert state.description == 'parana'

    def test_state_description_empty(self):
        with pytest.raises(ValueError):
            state = State('')

    def test_state_description_len(self):
        with pytest.raises(ValueError):
            state = State('nome aleatorio'*100)

    def test_state_description_int(self):
        with pytest.raises(TypeError):
            state = State(10)

    def test_state_id_country_str(self):
        with pytest.raises(TypeError):
            state = State('centro', '1')

    def test_state_id_country_lower_than_zero(self):
        with pytest.raises(ValueError):
            state = State('centro', -5)
'''