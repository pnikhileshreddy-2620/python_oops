a =[1,2,3]
b=a
print(id(a), id(b))
c = a[:]
print(id(c))
print(a==b and a==c)
print(a is  b)
print(a is b and a is c )