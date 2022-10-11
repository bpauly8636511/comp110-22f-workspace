"""Creating three functions to help invert, count highest occurance, and count frequency in dicts."""

__author__ = "730574853"

def invert(x: dict[str, str]) -> dict[str, str]:
    """This function takes the keys and values and inverts the two."""
    inverted = dict()
    for keys in x:
        inverted['keys'] = keys
    return inverted



def count(x: list[str]) -> dict[str, int]:
    """This function takes a list of strings and counts the occurances of each unique string."""
    new_keys: list[str] = ""
    second_index: int = 0
    for index in x:
        second_index += 1
        if index not in new_keys:
            new_keys += x[second_index]
    new_values: list[int] = ()
    counter: int = 0
    i: int = 0
    # please figure out the purpose of new_index
    new_index: str = index(index)
    for keys in new_keys:
        while i < len(x):
            if x[i] == new_keys[new_index]:
                counter += 0
                i += 1
            else:
                i += 1
        new_values += counter
    final_count = dict()
    for index in new_keys:
        final_count[index] += new_values[index]
    return final_count


def favorite_color(x: dict[str, str]) -> list[str]:
    """This function looks at the most common string in a dictionary and returns it."""
    count_list: list[str] = 0
    for keys in x:
        count_list += x[keys] 
    color_count: dict = count(count_list)
    final_list: list[str] = color_count[0]
    for keys in color_count:
        if color_count[keys] > color_count[final_list]:
            final_list = keys
        elif color_count[keys] == color_count[final_list]:
            final_list += keys
    return final_list