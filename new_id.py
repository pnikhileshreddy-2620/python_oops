my_list=[1,2,3,4,5]
print(id(my_list))

def display_element(items):
    print(id(items))
    for i in items:
        print(i)

display_element(my_list)