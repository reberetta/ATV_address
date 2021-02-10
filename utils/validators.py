from typing import Type


def validate_type(value: object, type: Type, key: str):
    if not isinstance(value, type):
        raise TypeError(f"{key.capitalize()} must be {type}.")
    return value


def validate_not_empty(value: object, key: str):
    if not value:
        raise TypeError(f"{key.capitalize()} can't be null.")
    elif str == type(value) and not value.strip():
        raise ValueError(f"{key.capitalize()} can't be empty.")
    return value


def validate_len(value: object, max_len: int, key: str):
    if len(value) > max_len:
        raise ValueError(f"{key.capitalize()} can't be greater than {max_len} characters.")
    return value


def validate_greater_than_zero(value: int, key: str):
    if value <= 0:
        raise ValueError(f"Value can't be lower than zero.")
    return value
