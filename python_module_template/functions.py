import math
from typing import List, Union


def add(
    a: Union[int, float, List[Union[int, float]]],
    b: Union[int, float, List[Union[int, float]]],
) -> Union[int, float, List[Union[int, float]]]:
    """
    Add two numbers or two lists element-wise.

    Parameters:
    a (int, float, or list): First operand.
    b (int, float, or list): Second operand.

    Returns:
    int, float, or list: The sum of the operands.
    """
    if not isIntOrFloat(a) or not isIntOrFloat(b):
        raise TypeError("Function parameters should be int or float")

    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise ValueError("Lists must have the same length")
        return [x + y for x, y in zip(a, b)]
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
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
    # Useless comment
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
