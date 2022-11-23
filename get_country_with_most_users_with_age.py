def get_country_with_most_users_with_age(data: list, age: int) -> str:
    """
    Return the country with the most users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        str: The country with the most users with the given age
    """
    for i in data:
        if i['age'] == age:
            return i['age']
    return -1


print(get_country_with_most_users_with_age([{'name': 'John', 'country': 'USA', 'age': 27}, {
      'name': 'Mary', 'country': 'UK', 'age': 42}], 27))
