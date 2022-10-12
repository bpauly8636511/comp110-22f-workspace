"""This runs test for the functions ivert, favorite color and count."""

__author__ = "730574853"

from dictionary import count, invert, favorite_color
import pytest

def test_invert() -> None:
    """The purpose of this is to do a case test to make sure the function works."""


def test_key_error() -> None:
    """The purpose of this is to do an edge case to make sure it raises a key error for repeat keys."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_large_strings() -> None:
    """The purpose of this is to do an edge case of large strings."""


def test_invert_same() -> None:
    """The purpose of this test is to do an edge case of dictionaries that have the same key and value."""