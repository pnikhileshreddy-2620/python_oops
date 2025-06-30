class Circle:
    def __init__(self,radius):
        self.radius =radius
    def find_radius(self):
        return self.radius*2

my_circle = Circle(10)
print(my_circle.find_radius())
