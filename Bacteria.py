class Bacteria:
    def __init__(self, name, shape, size, x=0, y=0):
        self.x=x
        self.y=y
        self.name=name
        self.shape=shape
        self.size=size

bactria = Bacteria("Bacilli","rod-shaped",(0.5 ,5 ),100,50)
bactria2=Bacteria("Cocci","sphere-shaped",(0.5,1.0),100,100)
bactria3=Bacteria("Spirilli","spiral-shaped",(15.0, 0.3),500,300)


Total = [bactria,bactria2,bactria3]

