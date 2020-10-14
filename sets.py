# Collection data type unordoered, mutable no duplicates
myset = {1, 2, 3, 4, 5, 6}
print(myset)

myset = {} # this will create empty dict
# if you want to create empty set you should
myset2 = set()
print(type(myset2))
myset1= set("Hello")
print(myset1)

myset2.add(1)
myset2.add(2)
myset2.add(3)
myset2.add(4)
myset2.add(5)
myset2.remove(3)
print(myset2) #Output 1,2,4,5
#myset2.discard(3) will remove the element,
#if it doesn't exist nothing will happen
print(myset2.pop())  #removes the first item

# myset2.clear() will clear the set 

for i in myset2:
    print(i)

if 4 in myset2:
    print(True)