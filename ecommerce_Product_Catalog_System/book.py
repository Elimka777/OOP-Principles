from .product import Product

class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Author: {self.author}"
