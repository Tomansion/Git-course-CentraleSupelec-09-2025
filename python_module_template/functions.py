from typing import Union
import math


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


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]):
    """
    Substract 1 number to another.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The substract of the two numbers.
    """
    return a - b


def squareRoot(a: Union[int, float]) -> Union[int, float]:
    """
    take in arg a number and give the square root

    Parameters:
    a (int or float)

    Returns:
    int or float: The square root of the number
    """
    if a < 0:
        return complex(0, math.sqrt(-a))

    return math.sqrt(a)
