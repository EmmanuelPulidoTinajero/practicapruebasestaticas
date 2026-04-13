from citysearch_data import CITY_NAMES


def CitySearch(query, cities=None):
    if cities is None:
        cities = CITY_NAMES

    if query == "*":
        return cities

    if len(query) < 2:
        return []

    query_lower = query.lower()
    return [city for city in cities if query_lower in city.lower()]