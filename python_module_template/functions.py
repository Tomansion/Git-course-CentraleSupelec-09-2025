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
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise ValueError("Lists must have the same length")
        return [x + y for x, y in zip(a, b)]
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise TypeError("Both arguments must be numbers or lists of the same length")


def subtract(a, b):
    return a - b
