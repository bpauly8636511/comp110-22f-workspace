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


    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates a range of values for simpy to be, each value increasing by step."""
        assert step != 0
        new_value: float = start 
        new_simpy: list[float] = []
        i: int = 0
        while i < stop:
            if i < 1:
                new_simpy.append(start)
            new_value += step
            new_simpy.append(new_value)
            i += 1
    

    def sum(self) -> float:
        """Summing all the values in Simpy."""
        final_sum: float = sum(self.values)
        return final_sum