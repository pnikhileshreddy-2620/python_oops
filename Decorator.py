class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        self._price=price
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        self._size=size
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self,brand):
        self._brand=brand