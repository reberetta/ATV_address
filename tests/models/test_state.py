import pytest
from models.state import State


class TestState:
    def test_state_instance():
        state = State('parana')
        assert isinstance(state, State)
        assert state.description == 'parana'

    def test_state_description_empty():
        with pytest.raises(ValueError):
            state = State('')

    def test_state_description_len():
        with pytest.raises(ValueError):
            state = State('nome aleatorio'*100)

    def test_state_description_int():
        with pytest.raises(TypeError):
            state = State(10)
