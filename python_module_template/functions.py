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


def divide(a, b):
    """
    Divide two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The division of the two numbers.
    """
    if a == 0 | b == 0:
        raise Exception("Divide by zero error")

    return a / b
