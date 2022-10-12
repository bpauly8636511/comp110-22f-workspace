"""Creating three functions to help invert, count highest occurance, and count frequency in dicts."""

__author__ = "730574853"

def invert(x: dict[str, str]) -> dict[str, str]:
    """This function takes the keys and values and inverts the two using lookup."""
    inverted = dict()
    for keys in x:
        inverted[x[keys]] = keys
    return inverted



def count(x: list[str]) -> dict[str, int]:
    """This function takes a list of strings and counts the occurances of each unique string."""
    keys: list[str] = []
    counter: int = 1
    final_dict = dict()
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


def favorite_color(x: dict[str, str]) -> list[str]:
    """This function looks at the most common string in a dictionary and returns it."""
    count_list: list[str] = []
    for keys in x:
        count_list.append(x[keys]) 
    color_count: dict = count(count_list)
    final_list: list[str] = color_count[0]
    for keys in color_count:
        if color_count[keys] > color_count[final_list]:
            final_list = keys
        elif color_count[keys] == color_count[final_list]:
            final_list.append(keys)
    return final_list