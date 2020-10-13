#Lists are ordered, mutable, allows duplicate values
mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item = mylist.remove("banana")
print(mylist)
mylist.sort()
print(mylist)

list1 = [4, 3, 1, -1, -5, 10]
list = sorted(list1)
print(list)

list2 = [0] * 5
print(list2)
list3 = [1, 2, 3, 4, 5]
list4 = list2 + list3 
print(list4)

mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Start index: end index
a = mylist1[2:5]
print(a)
b = mylist1[:5]
print(b)
c = mylist1[1:]
print(c)
print(mylist1[::2])
# this will reverse
print(mylist1[::-1])