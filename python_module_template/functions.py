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
    if not isIntOrFloat(a) or not isIntOrFloat(b):
        raise TypeError("Function parameters should be int or float")

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


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b


def power(a, b):
    if a == 0 and b == 0:
        return None
    return a**b
def divide(a, b) -> Union[int, float]:
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
