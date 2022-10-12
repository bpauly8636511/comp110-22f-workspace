"""Creating three functions to help invert, count highest occurance, and count frequency in dicts."""

__author__ = "730574853"


def invert(x: dict[str, str]) -> dict[str, str]:
    """This function takes the keys and values and inverts the two using lookup."""
    inverted = dict()
    for keys in x:
        inverted[x[keys]] = keys
        raise ValueError("More than one key occurance.")
    return inverted


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


def favorite_color(x: dict[str, str]) -> str:
    """This function looks at the most common string in a dictionary and returns it."""
    colors: list[str] = []
    for keys in x:
        colors.append(x[keys]) 
    count_colors: dict = count(colors)
    greatest_value: int = 0
    final_color: str = ""
    for strings in count_colors:
        if count_colors[strings] > greatest_value:
            final_color = strings
            greatest_value = count_colors[strings]
    return final_color