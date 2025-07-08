import array

arr =array.array('i',[5,10,15])
arr.pop(1)
print(arr)
print(arr[1])


print(object)
print(isinstance(object,int))
print(isinstance(5,object))
print(isinstance("n",object))
print(isinstance([1,2,3,4,5],object))

i=10
a=10
b=2
print(id(i))
print(id(a))
print(id(a)==id(i))
print(id(b))