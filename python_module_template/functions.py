from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    if not isIntOrFloat(a) or not isIntOrFloat(b):
        raise TypeError("Function parameters should be int or float")

    return a + b


def isIntOrFloat(vartotest):
    """
    Add an any type var.

    Parameters:
    vartotest

    Returns:
    true if vartotest is a float or an int, false otherwise
    """
    return isinstance(vartotest, (float, int))


def subtract(a, b):
    return a - b
