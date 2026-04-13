from barcode_data import PRODUCT_PRICES


class BarcodeApp:
    def __init__(self, product_prices=None):
        self.product_prices = PRODUCT_PRICES if product_prices is None else product_prices
        self.scanned_prices = []

    def scan(self, barcode):
        if barcode == "":
            return "Error: empty barcode"

        if barcode not in self.product_prices:
            return "Error: barcode not found"

        price = self.product_prices[barcode]
        self.scanned_prices.append(price)
        return f"${price:.2f}"

    def total(self):
    return f"${sum(self.scanned_prices):.2f}"