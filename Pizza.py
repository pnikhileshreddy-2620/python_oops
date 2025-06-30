class Pizza:
    PRICE=100
    def __init__(self, description,toppings, crust):
        self.description=description
        self.topping =toppings
        self.crust =crust

my_prizzq =Pizza("M","BASIL","New york")
my_prizzq.PRICE

print(my_prizzq.PRICE)
