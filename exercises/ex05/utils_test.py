"""This is where I am testing the functions in my utils file for ex05."""

__author__ = "730574853"

from utils import only_evens, sub, concat

def test_only_evens_empty() -> None:
    x: list[int] = []
    assert only_evens(x) == []


def test_only_evens_evens() -> None:
    x: list[int] = [0, 2, 4, 6]
    assert only_evens(x) == [0, 2, 4, 6]


def test_only_evens_mixed() -> None:
    x: list[int] = [2, 5, 6, 7, 9, 10, 12]
    assert only_evens(x) == [2, 6, 10, 12]


def test_concat_empty() -> None:
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_short() -> None:
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_concat_long() -> None:
    x: list[int] = [1, 4, 7, 3]
    y: list[int] = [6, 10, 2, 100, -5]
    assert concat(x, y) == [1, 4, 7, 3, 6, 10, 2, 100, -5]


def test_sub_empty() -> None:
    x: list[int] = []
    y: int = 20
    z: int = -3
    assert sub(x, y, z) == []


def test_sub_positive() -> None:
    x: list[int] = [2, 4, 6, 8, 10]
    y: int = 1
    z: int = 4
    assert sub(x, y, z) == [4, 6, 8]

def test_sub_negative() -> None:
    x: list[int] = [-2, -5, -6, 7, 8, 9]
    y: int = 2
    z: int = 3
    assert sub(x, y, z) == [-6]
    