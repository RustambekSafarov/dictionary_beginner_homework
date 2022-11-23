def find_max_value(data: dict) -> int:
    """
    Return the maximum value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    m = list(data.values())[0]
    for i in data.values():
        if m < i:
            m = i
    return m


print(find_max_value({'a': 1, 'b': 2, "c": 3}))
