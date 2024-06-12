# ecommerce/main.py

from ecommerce_Product_Catalog_System import Book, Electronic, Clothing

def main():
    # Creating instances of each subclass
    my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
    my_electronic = Electronic("456", "Smartphone", 499.99, "64GB, 4GB RAM")
    my_clothing = Clothing("789", "T-Shirt", 19.99, "L")

    # Displaying information of each product
    print(my_book.display_info())
    print(my_electronic.display_info())
    print(my_clothing.display_info())

if __name__ == "__main__":
    main()
