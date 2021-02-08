import pytest
from models.state import State


class TestState:
    def test_state_instance():
        state = State('rua amintas', 453, '34352-54')
        assert isinstance(state, State)
        assert state.description == 'rua amintas'
        assert state.number == 453
        assert state.cep == '34352-54'

    def test_state_name_empty():
        with pytest.raises(ValueError):
            state = State('')

    def test_state_name_len():
        with pytest.raises(ValueError):
            state = State('rua amintas'*100, 453, '34352-54')

    def test_state_name_int():
        with pytest.raises(TypeError):
            state = State(10)

    def test_state_number_empty():
        with pytest.raises(ValueError):
            state = State('rua amintas', None, '34352-54')

    def test_state_number_str():
        with pytest.raises(TypeError):
            state = State('rua amintas', '453', '34352-54')

    def test_state_description_empty():
        with pytest.raises(ValueError):
            state = State('rua amintas', 564, '')

    def test_state_description_len():
        with pytest.raises(ValueError):
            state = State('rua amintas', 453, '34352-54'*100)

    def test_state_description_int():
        with pytest.raises(TypeError):
            state = State('rua amintas', 453, 100)
