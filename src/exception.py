class ZeroQuantityException(Exception):
    """ Exception raised when adding a product with zero quantity """
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "You cannot add a product with zero quantity."
