import pytest
from python_module_template.functions import multiply


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
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


def test_multiply_asserts():
    assert multiply(1, 2) == 3
    assert multiply(-1, 1) == 0
    assert multiply(0, 0) == 0
    assert multiply(1.5, 2.5) == 4.0
    assert multiply(-1.5, -2.5) == -4.0