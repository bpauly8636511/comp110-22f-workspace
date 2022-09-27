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
    """This function takes two lists and adds the second to the end of the first."""
    concatenated_list: int = list()
    concatenated_list += x
    concatenated_list += y
    return concatenated_list


def sub(x: list[int], y: int, z: int) -> int:
    """This function takes a subset of the list inbetween the indexes given."""
    sub_list: int = list()
    i: int = y
    if y < 0:
        i: int = 0
        z -= 1
    elif z > len(x):
        z = len(x) - 1
    elif len(x) == 0 or y > len(x) or z <= 0:
        return sub_list
    while i <= z:
        sub_list += x[i]
        i += 1
    return sub_list