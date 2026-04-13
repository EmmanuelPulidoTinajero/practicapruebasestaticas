import pytest
from citysearch import CitySearch
from citysearch_data import CITY_NAMES

city = [
        ("", []),
        ("1", []),
        ("V", []),
        ("Va", ["Valencia", "Vancouver"]),
        ("va", ["Valencia", "Vancouver"]),
        ("vA", ["Valencia", "Vancouver"]),
        ("ape", ["Budapest"]),
        ("York", ["New York City"]),
        ("*", CITY_NAMES),
]


@pytest.mark.parametrize("query, expected", city)
def test_citysearch(query, expected):
    assert CitySearch(query) == expected


def test_citysearch_with_custom_data_set():
        custom_cities = ["Madrid", "Malaga", "Malmo", "Lisbon"]

        assert CitySearch("ma", custom_cities) == ["Madrid", "Malaga", "Malmo"]
    