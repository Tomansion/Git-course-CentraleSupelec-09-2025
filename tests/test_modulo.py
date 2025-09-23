import pytest
from python_module_template.functions import modulo


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 1),
        (15, 6, 3),
        (-1, 1, 0),
        (5.5, 2, 1.5),
        (16, 2.5, 1.0),
        (5, 0, "no division by 0"),
    ],
)
def test_modulo(a, b, expected):
    assert modulo(a, b) == expected
