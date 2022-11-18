"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730574853"


class Simpy:
    """Making a class that has a list of floats."""
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
            assert len(self.values) == len(rhs.values)
            new_value: Simpy = ()
            i: int = 0
            while i < len(self.values):
                new_value = self.values[i] + rhs.values[i] 
                added_simpy.append(new_value)
                i += 1
            return added_simpy
        if isinstance(rhs, float):
            for nums in self.values:
                new_value = nums + rhs
                added_simpy.append(new_value)
            return added_simpy

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """This is very similar to add but instead it is supposed to take self to an exponentiation of a float or simpy value."""
        exponentiated_simpy: list[Simpy] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_values: Simpy = ()
            i: int = 0
            while i < len(self.values):
                new_values = self.values[i] ** rhs.values[i]
                exponentiated_simpy.append(new_values)
                i += 1
            return exponentiated_simpy
        if isinstance(rhs, float):
            for floats in self.values:
                new_values = floats ** rhs
                exponentiated_simpy.append(new_values)
            return exponentiated_simpy

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Taking Simpy values and directly comparing them with another Simpy or float value to make a list of boolean values."""
        mask: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_value: Simpy = ()
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    new_value = True
                else:
                    new_value = False
                mask.append(new_value)
                i += 1
            return mask
        if isinstance(rhs, float):
            for values in self.values:
                if values == rhs:
                    new_value = True
                else:
                    new_value = False
                mask.append(new_value)
            return mask

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Similar to eq except this time testing for greater than."""
        mask_two: list[bool] = []
        new_value: Simpy = ()
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    new_value = True
                else:
                    new_value = False
                mask_two.append(new_value)
                i += 1
            return mask_two
        if isinstance(rhs, float):
            for values in self.values:
                if values > rhs:
                    new_value = True
                else:
                    new_value = False
                mask_two.append(new_value)
            return mask_two
            
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Using subscription annotation to identify a value of a Simpy at a certain index or true value."""
        if isinstance(rhs, int):
            final: Simpy = list()
            i: int = 0
            while i <= rhs:
                final = self.values[i]
                i += 1
            return final
        else:
            assert len(self.values) == len(rhs)
            i: int = 1
            new_simpy: Simpy = list()
            while i < len(self.values):
                if rhs[i]:
                    new_simpy.append(self.values[i])
                    i += 1
                else:
                    i += 1
            return new_simpy
