"""fibonacci with for loop
"""


def fibonacci(number: int) -> list:
    """calculate the fibonacci numbers from 0 to number

   Args:
        number(int): index of fibonacci numbers

    Returns:
        list: list of fibonacci numbers
    """
    first, second = 0, 1
    result = []
    for _ in range(1, number+1):
        result.append(first)
        first, second = second, first + second
    return result
