import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.

    Args:
        condition: A function that takes a dictionary and returns True or False.
        dict_list: A list of dictionaries.

    Returns:
        A list of dictionaries for which condition(item) is True.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]
        >>> filter_items(lambda s: s["score"] >= 85, students)
        [{'name': 'Alice', 'score': 90}, {'name': 'Charlie', 'score': 85}]

        >>> filter_items(lambda s: s["name"].startswith("A"), students)
        [{'name': 'Alice', 'score': 90}]

        >>> filter_items(lambda s: s["score"] > 100, students)
        []
    """
    result = []
    for item in dict_list:
        if condition(item):
            result.append(item)
    return result

def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.

    Args:
        aggregation_key: The dictionary key whose values should be aggregated.
        aggregation_function: A function such as sum, max, min, etc.
        dict_list: A list of dictionaries.

    Returns:
        The aggregated result.

    Examples:
        >>> students = [
        ...     {"name": "Alice", "score": 90},
        ...     {"name": "Bob", "score": 70},
        ...     {"name": "Charlie", "score": 85}
        ... ]

        >>> aggregate("score", sum, students)
        245

        >>> aggregate("score", max, students)
        90

        >>> aggregate("score", min, students)
        70

        >>> aggregate(
        ...     "score",
        ...     lambda scores: sum(scores) / len(scores),
        ...     students
        ... )
        81.66666666666667
    """
    value = []
    for item in dict_list:
        value.append(float(item[aggregation_key]))
    return aggregation_function(value)


# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
avg_all = aggregate('temperature', lambda temps: sum(temps) / len(temps), cities)
print(avg_all)
print()


# Print all cities in Germany
print("All cities in Germany")
germany_cities = filter_items(lambda c: c['country'] == 'Germany', cities)
for city in germany_cities:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
spain_warm_cities = filter_items(lambda c: c['country'] == 'Spain' and float(c['temperature']) > 12, cities)
for city in spain_warm_cities:
    print(city)
print()


# Count the number of unique countries

uniqe_countries = set(city['country'] for city in cities)
print(f"Number of unique countries:",len(uniqe_countries))
print()

# Print the average temperature for all the cities in Germany
germany_cities = filter_items(lambda c: c['country'] == 'Germany', cities)
avg_germany_temp = aggregate('temperature', lambda temps: sum(temps) / len(temps), germany_cities)
print(f"The average temperature for all the cities in Germany: {avg_germany_temp:.2f}")
print()

# Print the max temperature for all the cities in Italy
italy_cities = filter_items(lambda c: c['country'] == 'Italy', cities)
max_temp_italy = aggregate('temperature', max, italy_cities)
print(f"The max temperature for all the cities in Italy {max_temp_italy:.2f}")
