class CashRegister:
    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.items = {}

    def add_product(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}
        return self

    def display_items(self):
        print(f"\nCashier: {self.cashier_name}")
        print("Products in current purchase:")
        for name, info in self.items.items():
            print(f"{name} - ₹{info['price']} x {info['quantity']}")
        return self

    def find_the_item(self, item_name):
        if item_name in self.items:
            print(f"{item_name} is in the cart.")
        else:
            print(f"{item_name} not found.")

    def removing_item(self, item_name):
        if item_name in self.items:
            self.items.pop(item_name)
            print(f"{item_name} removed.")
        else:
            print("Item not found.")
        return self

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name]['price'] = new_price
            print(f"{item_name} price updated to ₹{new_price}")
        else:
            print("Invalid item")
        return self

    def find_subtotal(self):
        subtotal = sum(info['price'] * info['quantity'] for info in self.items.values())
        print(f"Subtotal: ₹{subtotal:.2f}")
        return subtotal

    def find_tax(self):
        tax = self.find_subtotal() * 0.05
        print(f"Tax (5%): ₹{tax:.2f}")
        return tax

    def total_amount(self):
        total = self.find_subtotal() + self.find_tax()
        print(f"Total Amount: ₹{total:.2f}")
        return total

    def clear_purchase(self):
        self.items.clear()
        print("Purchase cleared.")
        return self


register = CashRegister("Nikhilesh")

register.add_product("Book", 25, 2)\
        .add_product("Pen", 10)\
        .add_product("Pad", 50)\
        .display_items()

register.find_the_item("Pen")
register.removing_item("Book").display_items()
register.update_price("Pad", 60)
register.find_subtotal()
register.find_tax()
register.total_amount()
register.clear_purchase().display_items()
