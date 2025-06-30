class Player:
    def __init__(self, x, y):
        self.x=x
        self.y =y
    def move_up(self, change=5):
        self.y+=change
    def move_down(self,change=5):
        self.y-=change
    def move_right(self,change=5):
        self.y+=change
    def move_left(self,change=5):
        self.y-=change

myPlayer = Player(10,10)
print(myPlayer.x, myPlayer.y)
myPlayer.move_up()
print(myPlayer.x, myPlayer.y)
myPlayer.move_up(1)
print(myPlayer.x, myPlayer.y)
