"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730574853"


class Simpy:
    values: list[float]

    # TODO: Your constructor and methods will go here.
    def __init__(self, values: list[float]):
        """Constructs the values attribute as the argument passed."""
        self.values = values


    def __repr__(self) -> str:
        """Taking the points in the simpy class and turning them into a list of strings."""
        return f"Simpy({self.values})"


    def fill(self, number: float, number_filled: int) -> None:
        """Taking the values of simpy and mutating it to be filled wih a number of new repeating floats."""
        new_simpy: list[float] = []
        for i in range(number_filled):
            new_simpy.append(number)
        self.values = new_simpy



