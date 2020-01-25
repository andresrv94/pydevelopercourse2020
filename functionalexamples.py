#map, filter, zip

my_list=[1,2,3,4,5]
second_list= [2,3,3,3]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0


print(list(map(multiply_by2,my_list))) #Using map function
print(list(filter(only_odd,my_list))) #Using filter function

print(list(zip(my_list,second_list)))
#print(my_list)