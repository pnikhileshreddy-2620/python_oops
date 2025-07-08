def add(a,b=2):
    return a+b
print(add(3))

def modify(a):
    a = a+[4,5]
    return a

x= [1,2,3]
modify(x)
print(x)
print(modify(x))