from Human_Data import person

a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(id(a))
print(id(b))
print(a is b)
print(a==b)


c=(1,2,3,4,5)
d=(1,2,3,4,5)
print(id(c),id(d))
print(c==d)
print(c is d)

name="Nikhilesh"
last="Nikhilesh"
print(name is last)

print(name==last)
print("------------------------")
ext ="Nikhilesh"
print(id(ext))
l_ext=ext
print(l_ext, id(l_ext))
l_ext="Reddy"
print(l_ext)
print(ext)

print("---------------------------")

new_list =[1,2,3,4,5]
ext_list=new_list
print(id(new_list),id(ext_list))

ext_list =[10,11,21]
print(id(new_list),id(ext_list))