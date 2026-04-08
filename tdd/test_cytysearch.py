import pytest
from citysearch import CitySearch
city = [("", []), 
        ("1", []),
        ]
@pytest.mark.parametrize("query, expected", city)
def test_citysearch(query, expected):
    assert CitySearch(query) == expected
    