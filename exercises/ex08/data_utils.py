"""Dictionary related utility functions."""

__author__ = "730574853"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], row_amount: int) -> dict[str, list[str]]:
    """Produce a new column based table with only the first amount wanted of rows."""
    final_head: dict[str, list[str]] = {}
    for columns in table:
        first_values: list[str] = []
        for items in range(row_amount):
            first_values.append(table[columns][items])
        final_head[columns] = first_values
    return final_head


def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new table but only with a certain subset of original columns."""
    final_selection: dict[str, list[str]] = {}
    for columns in column_names:
        final_selection[columns] = table[columns]
    return final_selection


def concat(table: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Producing a new column based table with two previous column based tables combined."""
    final_dict: dict[str, list[str]] = {}
    for columns in table:
        final_dict[columns] = table[columns]
    for keys in table_two:
        if keys in final_dict:
            final_dict[keys] = table_two[keys] + table[keys]
        else:
            final_dict[keys] = table_two[keys]
    return final_dict


def count(x: list[str]) -> dict[str, int]:
    """This function takes a list of strings and counts the occurances of each unique string."""
    keys: list[str] = []
    counter: int = 1
    final_dict: dict[str, int] = dict()
    for values in x:
        if values not in keys:
            keys.append(values)
    values_list: list[int] = []
    i: int = 0
    for strings in keys:
        counter = 0
        i = 0
        while i < len(x):
            if strings == x[i]:
                counter += 1
                i += 1
            else: 
                i += 1
        values_list.append(counter)
    for index in range(len(keys)):
        final_dict[keys[index]] = values_list[index]
    return final_dict