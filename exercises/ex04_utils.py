"""Using list utilities to create well known python functions!"""

__author__ = "730547853"

def all(input: list[int], int: int) -> bool:
    """A function that checks each integer in a list to see if they all match the integer given."""
    if len(input) < 1:
        return False
    i: int = 0
    while i <= len(input):
        if int != input[i]:
            return False
        else:
            i += 1


def max(input: list[int]) -> int:
    """A function that will return the greatest number from a list of integers given."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    max_value: int = 0
    i: int = 0
    while i <= len(input):
        if input[i] > max_value:
            max_value = input[i]
            i += 1
        else:
            i += 1
    return max_value

def is_equal(input: list[int], input_two: list[int]) -> bool:
    """A function that will check to lists of integers to make sure they are deeply equal; constituted of the exact same values at each index."""
    i: int = 0
    if len(input) == len(input_two):
        while i < len(input):
            if input[i] != input_two[i]:
                return False
            else:
                i += 1
    return True



