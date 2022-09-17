"""Using list utilities to create well known python functions!"""

__author__ = "730547853"

def all(input: list[int], int: int) -> bool:
    """A function that checks each integer in a list to see if they all match the integer given."""
    if len(input) < 1:
        return False
    elif 


def max(input: list[int]) -> int:
    """A function that will return the greatest number from a list of integers given."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")


def is_equal(input: list[int], input_two: list[int]) -> bool:
    """A function that will check to lists of integers to make sure they are deeply equal; constituted of the exact same values at each index."""


