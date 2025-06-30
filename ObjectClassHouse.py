class BlackPack:
    def __init__(self):
        self.item=[]

mypack=BlackPack()
mypack.item.append("Back")
mypack.item.append("5 zip")
mypack.item.append(1000)
for items in mypack.item:
    print(items)
