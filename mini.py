class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        return self._price
    def get_size(self):
        return self._size
    def get_brand(self):
        return self._brand
    def set_price(self,price):
        self._price=price
    def set_size(self,size):
        self._size=size
    def set_brand(self,brand):
        self._brand=brand

    price=property(set_price,get_price)
    brand=property(get_brand,set_brand)
    size=property(set_size,get_size)


