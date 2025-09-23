import pytest
from python_module_template.functions import power


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 8),
        (-2, 1, -2),
        (2, -1, 0.5),
        (-1, -3, -1.0),
        (0, 0, None),
    ],
)
def test_power(a, b, expected):
    assert power(a, b) == expected


def test_power_asserts():
    assert power(2, 3) == 8
    assert power(-2, 1) == -2
    assert power(2, -1) == 0.5
    assert power(-1, -3) == -1.0
    assert power(0, 0) is None
