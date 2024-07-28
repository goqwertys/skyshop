class Product:
    """ Represents a product """
    def __init__(self, name: str, description: str, price: float, count: int):
        """ Initialization of a new product """
        self.name = name
        self.description = description
        self.price = price
        self.count = count


class Category:
    """Represents a category of products"""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        """ Initialization of a category """
        self.name = name
        self.description = description
        self.products = []
        Category.category_count += 1

    def add_product(self, product: Product):
        """ Add product to products list """
        if product not in self.products:
            self.products.append(product)
            Category.product_count += 1
