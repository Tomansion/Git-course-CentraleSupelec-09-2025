import pytest
from python_module_template.functions import add, squareRoot


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
    assert squareRoot(4) == 2


def test_add_asserts():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, -2.5) == -4.0