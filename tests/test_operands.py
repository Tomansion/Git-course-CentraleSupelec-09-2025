import pytest
from python_module_template.functions import (
    add,
    subtract,
    multiply,
    power,
    divide,
    modulo,
)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
        (-1.5, -2.5, -4.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, -1),
        (-1, 1, -2),
        (0, 0, 0),
        (1.5, 2.5, -1.0),
        (-1.5, -2.5, 1.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 2),
        (-1, 1, -1),
        (0, 0, 0),
        (1.5, 2.5, 3.75),
        (-1.5, -2.5, 3.75),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 1),
        (-1, 1, -1),
        (0, 0, None),
        (3, 4, 81),
        (4, 0.5, 2),
    ],
)
def test_power(a, b, expected):
    assert power(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 0.5),
        (-1, 1, -1),
        (0, 0, None),
        (1.5, 2.5, 0.6),
        (-1.5, -2.5, 0.6),
    ],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 1),
        (-1, 1, 0),
        (0, 0, None),
        (1.5, 2.5, 1.5),
        (4, 3, 1),
        (-1.5, -2.5, -1.5),
    ],
)
def test_modulo(a, b, expected):
    assert modulo(a, b) == expected
