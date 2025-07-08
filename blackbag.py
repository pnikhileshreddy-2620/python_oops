class Backbag:
    def __init__(self,):
        self.item=[]


    def item(self):
        return self.item

    def add_items(self,items):
        if isinstance(items,str):
            self.item.append(items)
        else:
            print("Please provide the valid data")
    def remove_items(self,items):
        if isinstance(items,str) and items  in self.item:
            self.item.remove(items)
            return 1
        else:
            print("ITEM NOT FOUND")
            return 0
    def find_the_items(self,items):
        if isinstance(items,str) and items in self.item:
            return 1
        else:
            return 0

backbag= Backbag()
print(backbag.item)
backbag.add_items("Back color")
backbag.add_items("Water Bottle")
value=backbag.find_the_items("bag")
print(backbag.find_the_items("Back color"))
print(value)
print(backbag.item)
print(backbag.find_the_items("Back color"))
backbag.remove_items("Nikhilesh")
print(backbag.item)
backbag.remove_items("Water Bottle")
print(backbag.item)
# using class name we are calling the methods 
Bag =Backbag()
Backbag.add_items(Bag,"White")

backbag1= Backbag()
backbag.add_items("pink color")

print(id(backbag))
print(id(backbag1))