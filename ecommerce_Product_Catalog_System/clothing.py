from .product import Product

class Clothing(Product):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Size: {self.size}"
