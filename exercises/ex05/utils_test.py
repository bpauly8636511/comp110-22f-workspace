"""This is where I am testing the functions in my utils file for ex05."""

__author__ = "730574853"

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Edge testing the only_evens function, that if there was an empty list entered it would give an empty list."""
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_evens() -> None:
    """Case testing to ensure only_evens works when numbers are even in the list."""
    x: list[int] = [0, 2, 4, 6]
    assert only_evens(x) == [0, 2, 4, 6]


def test_only_evens_mixed() -> None:
    """Case testing to ensure only even numbers are given with only_even function."""
    x: list[int] = [2, 5, 6, 7, 9, 10, 12]
    assert only_evens(x) == [2, 6, 10, 12]


def test_concat_empty() -> None:
    """Edge testing for an empty list to be given when adding to empty lists."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_order() -> None:
    """Case testing that the list comes out in order."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_concat_mixed() -> None:
    """Case testing that the list still works no matter what the list contains."""
    x: list[int] = [1, 4, 7, 3]
    y: list[int] = [6, 10, 2, 100, -5]
    assert concat(x, y) == [1, 4, 7, 3, 6, 10, 2, 100, -5]


def test_sub_empty() -> None:
    """Edge testing to make sure when an empty list is given that there is an empty list returned."""
    x: list[int] = []
    y: int = 20
    z: int = -3
    assert sub(x, y, z) == []


def test_sub_positive() -> None:
    """Case testing to ensure that the list given multiple numbers in the subset is returned."""
    x: list[int] = [2, 4, 6, 8, 10]
    y: int = 1
    z: int = 4
    assert sub(x, y, z) == [4, 6, 8]


def test_sub_negative() -> None:
    """Case testing to ensure that any numbers given and that the range being only one the one number is given even if the input isn't positive."""
    x: list[int] = [-2, -5, -6, 7, 8, 9]
    y: int = 2
    z: int = 3
    assert sub(x, y, z) == [-6]