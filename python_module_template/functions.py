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


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The difference of the two numbers.
    """
    return a - b
