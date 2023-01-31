from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __next__(self):
        try:
            product_inventory = self.products[self.index]
        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return product_inventory
