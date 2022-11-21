def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    numbers = []
    for i in data.keys():
        print(i)
        if str(i).isdigit():
            numbers.append(i)
    return numbers
print(find_int_keys({'a': 1, 3: 2, 'c': 3,10:'a'}))