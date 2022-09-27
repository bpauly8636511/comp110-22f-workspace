"""This is where the skeletions of the functions I will be implementing for ex05."""

__author__ = "730574853"


def only_evens(x: list[int]) -> list[int]:
    """This takes a list of ints and returns the even numbers in the list."""
    i: int = 0
    list_of_evens: list[int] = []
    for i in x:
        if i % 2 == 0:
            list_of_evens.append(i)
    return list_of_evens


def concat(x: list[int], y: list[int]) -> list[int]:
    """This function takes two lists and adds the second to the end of the first."""
    concatenated_list: list[int] = []
    concatenated_list += x
    concatenated_list += y
    return concatenated_list


def sub(x: list[int], y: int, z: int) -> list[int]:
    """This function takes a subset of the list inbetween the indexes given."""
    sub_list: list[int] = []
    i: int = y
    if y < 0:
        i = 0
    elif z >= len(x):
        z = len(x) - 1
    elif len(x) == 0 or y >= len(x) or z <= 0:
        return sub_list
    while i < z:
        sub_list.append(x[i])
        i += 1
    return sub_list