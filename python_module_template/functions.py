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
    return a + b


def subtract(a, b):
    return a - b


def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, str]:
    """
    Modulo two numbers.
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    Returns:
    int, float or str: The remainder when a is divided by b or "no division by 0" if b = 0.
    """
    if b == 0:
        return "no division by 0"
    return a % b
