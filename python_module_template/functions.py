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
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b


def power(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a**b if a != 0 and b != 0 else None


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    try:
        return a / b
    except ZeroDivisionError:
        print(f"You're really training to divide by {b}?? What a rascal...")
        # It's just to boost the code coverage in the tests with this exceptional case
        return None


def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    try:
        return a % b
    except ZeroDivisionError:
        print(f"{a}%{b}... are you serious?!")
        return None
