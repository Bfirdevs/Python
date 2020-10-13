#Tuple: ordered, immutable, allows duplicate elements
#The difference between list is tuple is immutable, tuple is not immutable
#we can use paranthsis with tuple, it works without paranthesis as well

mytuple = ("Max", "Tim", "Jim", "Kim")
print(mytuple)
print(type(mytuple))

#creating tuple from iterable
mytuple1 = (["Firdevs", "Elif", "Sinan"])
item = mytuple1[1]
item1 = mytuple1[-1]
print(item)
# will not work because tuple is immutable
#item[0] = "Hatice"
print(item1)

for i in mytuple1:
    print(i)
if "Elif" in mytuple1:
    print(True)
else:
    print(False)

mytuple2 = ('a', 'p', 'p', 'l', 'e')
print(len(mytuple2))
print(mytuple2.count('p'))
print(mytuple2.index('l'))
#we can easily convert from list to tuple / tuple to list 
mylist= list(mytuple2)
print(mylist)
mytuple3 = tuple(mylist)


a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
c = a[2:]
print(c)
d= a[::2]
print(d)
# reversing tuple
e = a[::-1]
print(e)

