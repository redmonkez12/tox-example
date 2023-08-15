from collections import defaultdict


class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Product: {self.name} Price: {self.price}"


class ShoppingCart:
    def __init__(self, max_item: int) -> None:
        self.items = defaultdict(int)
        self._total = 0
        self._max_item = max_item

    def add_item(self, item: Product, quantity: int) -> None:
        if self._total + quantity > self._max_item:
            raise Exception("Toto se ti nevleze do kosiku")

        if item.quantity - quantity < 0:
            raise Exception("Tolik rohliku nemame na sklade")

        item.quantity -= quantity

        self._total += quantity
        self.items[item] += quantity

    def remove_item(self, item: Product, quantity: int) -> None:
        if item not in self.items:
            raise Exception("Tato polozka neni v kosiku")

        # for cart_item, item_quantity in self.items.items():
        #     if cart_item == item:
        if self.items[item] - quantity < 0:
            raise Exception("Tolik polozek nemas v kosiku")

        self.items[item] -= quantity
        if self.items[item] == 0:
            del self.items[item]

    def get_total_price(self):
        total = 0
        for cart_item, quantity in self.items.items():
            total += quantity * cart_item.price

        return total

    def get_total_count(self):
        return self._total


# products = []
#
# for _ in range(100):
#     products.append(Product("Rohlik", 2.90))


# products = {
#     "product": Product("Rohlik", 2.90),
#     "quantity": 1000,
# }

products = [Product("Rohlik", 2.90, 10000)]
