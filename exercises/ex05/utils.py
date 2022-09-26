"""This is where the skeletions of the functions I will be implementing for ex05."""

__author__ = "730574853"

def only_evens(x: list[int]) -> int:
    """This takes a list of ints and returns the even numbers in the list."""
    i: int = 0
    list_of_evens: int = list()
    for int in len(x):
        if x[i] % 2 == 0:
            list_of_evens += x[i]
            i += 1
        else:
            i += 1


def concat(x: list[int], y: list[int]) -> int:
