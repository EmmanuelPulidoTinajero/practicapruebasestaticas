import pytest

from barcode_app import BarcodeApp
from barcode_data import PRODUCT_PRICES


scan_cases = [
    ("12345", "$7.25"),
    ("23456", "$12.50"),
    ("99999", "Error: barcode not found"),
    ("", "Error: empty barcode"),
]


@pytest.mark.parametrize("barcode, expected", scan_cases)
def test_scan_displays_expected_result(barcode, expected):
    app = BarcodeApp()

    assert app.scan(barcode) == expected


def test_total_returns_sum_of_scanned_items():
    app = BarcodeApp()

    app.scan("12345")
    app.scan("23456")

    assert app.total() == "$19.75"


def test_app_works_with_custom_product_catalog():
    custom_prices = {
        "A1": 1.25,
        "B2": 2.50,
        "C3": 3.75,
    }
    app = BarcodeApp(custom_prices)

    app.scan("A1")
    app.scan("C3")

    assert app.total() == "$5.00"


def test_default_catalog_contains_required_products():
    app = BarcodeApp()

    assert app.scan("12345") == f"${PRODUCT_PRICES['12345']:.2f}"