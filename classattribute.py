class main:
    Check =10
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 =num2

m1 = main(1,2)
m2= main(3,4)
m3=main(5,6)
print(m3.Check)
print(m1.Check)
main.Check=100
print(m3.Check)