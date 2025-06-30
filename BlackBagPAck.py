


class BackPackBag:
    def __init__(self):
        self.items=[]

    @property
    def item(self):
        return self.items

    @item.setter
    def item(self, value):
        if isinstance(value,str):
            self.item.append(value)
        else:
            print("please enter valid data")
    def show_detalis(self):
        for i in self.items:
            print(i)
        print(1)
b =BackPackBag()
b.item="BLACK"
b.item="five zip"
b.item="10 kg"
b.item="laptop bag"

print("----",b.show_detalis())




