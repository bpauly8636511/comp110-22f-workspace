"""This runs test for the functions ivert, favorite color and count."""

__author__ = "730574853"

from dictionary import count, invert, favorite_color
import pytest

def test_invert() -> None:
    """The purpose of this is to do a case test to make sure the function works."""
    x = {"UNC": "FUN", "DUKE": "LAME"}
    assert invert(x) == {"FUN": "UNC", "LAME": "DUKE"}


def test_key_error() -> None:
    """The purpose of this is to do an edge case to make sure it raises a key error for repeat keys."""


def test_invert_large_strings() -> None:
    """The purpose of this is to do an edge case of a large dictionary."""
    x = {"UNC": "FUN", "DUKE": "LAME", "COMP110": "IS SUPER AWESOME", "MARY": "HAD A LITTLE LAMB", "THIS DICT": "IS LONG"}
    assert invert(x) == {"FUN": "UNC", "LAME": "DUKE", "IS SUPER AWESOME": "COMP110", "HAD A LITTLE LAMB": "MARY", "IS LONG": "THIS DICT"}



def test_invert_same() -> None:
    """The purpose of this test is to do an edge case of dictionaries that have the same key and value."""
    x = {"UNC": "UNC", "DUKE": "DUKE"}
    assert invert(x) == {"UNC": "UNC", "DUKE": "DUKE"}


def test_count() -> None:
    """The purpose of this test is to do a case test to make sure that the basic function works."""
    x: list[str] = ["UNC", "UNC", "UNC", "DUKE", "DUKE"]
    assert count(x) == {"UNC": 3, "DUKE": 2}


