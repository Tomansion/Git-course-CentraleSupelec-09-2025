import pytest
from python_module_template.functions import squareRoot


def test_square_root():
    assert squareRoot(4) == 2
    assert squareRoot(9) == 3
    assert squareRoot(0) == 0
    assert squareRoot(2.25) == 1.5
