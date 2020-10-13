list_org = ["banana", "cherry", "apple"]
#they refer to same list inside the memory
#list_copy = list_org
#list_copy.append("lemon")
#output will be same for both
#print(list_copy)
#print(list_org)


list1 = list_org.copy()
list1.append("lemon")
print(list1)
list2 = list(list_org)
list2.append("ananas")
print(list2)
list3 = list_org[:]
print(list3)
#efficient and fast way to create a new list from an existing list
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [i*i for i in mylist]
print(mylist)
print(b)