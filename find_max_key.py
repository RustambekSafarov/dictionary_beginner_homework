def find_max_key(data: dict) -> int:
    """
    Return the maximum key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    s = list(data.keys())[0]
    for i in data.keys():
        if int(i) > s:
            s = i
    return s


print(find_max_key({1: 'a', 2: 'b', 3: 'c'}))
