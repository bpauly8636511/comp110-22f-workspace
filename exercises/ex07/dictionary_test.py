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


def test_count_no_repeats() -> None:
    """The purpose of this test is to do an edge case that will check for no repeats in the list."""
    x: list[str] = ["UNC", "IS", "THE BEST"]
    assert count(x) == {"UNC": 1, "IS": 1, "THE BEST": 1}


def test_count_one_repeat() -> None:
    """The purpose of this test is to do an edge case that will check for when theres only one repeated value."""
    x: list[str] = ["UNC", "UNC", "UNC", "UNC", "DUKE"]
    assert count(x) == {"UNC": 4, "DUKE": 1}


def test_favorite_color() -> None:
    """The purpose of this case test is to make sure that the basic function favorite colors works."""
    x = {"BROOKE": "BLUE", "GAVIN": "RED", "WILL": "RED", "ADORA": "PINK", "MOM": "GREEN"}
    assert favorite_color(x) == "RED"


def test_favorite_color_once() -> None:
    """The purpose of this test it to do an edge case that will check for when there is only one favorite color."""
    x = {"Brooke": "BLUE"}
    assert favorite_color(x) == "BLUE"


def test_favorite_color_even() -> None:
    """The purpose of this test is to do an edge case that will check for when there is colors equally liked."""
    x = {"BROOKE": "BLUE", "GAVIN": "RED", "ADORA": "PINK"}
    assert favorite_color(x) == "BLUE"