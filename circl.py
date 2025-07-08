class Circle:
    def __init__(self, radius):
        self.radius= radius

my_circl = Circle(5)
your_circl = my_circl
print(my_circl.radius)
print(your_circl.radius)
your_circl.radius=10

new_cir = Circle(10)
print(id(my_circl), id(your_circl))
print(id(new_cir))
print("Third object",new_cir.radius)

print(my_circl.radius)
print(your_circl.radius)