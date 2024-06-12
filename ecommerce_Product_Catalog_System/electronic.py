from .product import Product

class Electronic(Product):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Specs: {self.specs}"
