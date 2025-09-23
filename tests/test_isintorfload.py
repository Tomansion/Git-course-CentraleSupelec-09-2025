from python_module_template.functions import isIntOrFloat


def test_isIntOrFloat_asserts():
    assert isIntOrFloat(1) is True
    assert isIntOrFloat(1.0) is True
    assert isIntOrFloat("Fail") is False
