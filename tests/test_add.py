import pytest
from python_module_template.functions import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
        (-1.5, -2.5, -4.0),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_add_asserts():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(-1.5, -2.5) == -4.0
    with pytest.raises(TypeError):
        assert add("Fail", "Test")
