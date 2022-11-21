def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    s = 0
    for i in data.values():
        s += len(i)
    return s
print(find_length_of_values({'a': 'abc', 'b': 'def', 'c': 'ghi'}))