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
        assert step != 0.0
        new_value: float = start
        new_simpy: list[float] = [start]
        i: float = start
        stop = stop - step
        if step > 0.0:
            while i < stop:
                new_value += step
                new_simpy.append(new_value)
                i += step
        if step < 0.0:
            while i > stop:
                new_value += step
                new_simpy.append(new_value)
                i += step
        self.values = new_simpy

    

    def sum(self) -> float:
        """Summing all the values in Simpy."""
        final_sum: float = sum(self.values)
        return final_sum
    

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Ädding a left hand variable of a simpy type to a right hand side variable that is a Simpy or float type."""
        added_simpy: list[Simpy] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs)
            new_value: Simpy = ()
            for i in range(self.values):
                new_value = rhs[i] + self.values[i]
                added_simpy.append(new_value)
            return added_simpy
        if isinstance(rhs, float):
            for nums in self.values:
                new_value = nums + rhs
                added_simpy.append(new_value)
            return added_simpy
        

