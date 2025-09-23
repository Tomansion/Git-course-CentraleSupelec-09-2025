import pytest
from python_module_template.functions import divide


@pytest.mark.parametrize(
    "a, b, expected",
    [(2, 1, 2), (5, 2, 2.5)],
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_asserts():
    assert divide(2, 1) == 1
    assert divide(5, 2) == 2.5
