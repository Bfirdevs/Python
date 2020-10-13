#tuple ordered, immutable, allows duplicate elements
import sys
my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print(name)
print(age)
print(city)

tuple1 = (0, 1, 2 ,3, 4, 5, 6)
#i1 is first item, i3 is last item, *i2 is all the items between i1 and i3 
i1, *i2, i3 = tuple1

print(i1)
print(i2)
print(i3)

my_list = [0, 1, 2, "hello", True]
my_tuple1 = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes") #output is 120 bytes 
print(sys.getsizeof(my_tuple1), "bytes") # output is 80 bytes  list is largen eventhough they have the same element

#working with tuple much more efficient than working with list because the time is less to create tuple and size is less as well