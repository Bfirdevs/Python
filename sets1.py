odds = {1, 3, 5, 7, 9, 11}
evens = {0, 2, 4, 6, 8, 10}
primes = {2, 3, 5, 11}
 # union combines two set without duplication
u = odds.union(evens)
print(u) 
#intersection prints the same elements
i = odds.intersection(evens)
print(i)

i1 = odds.intersection(primes)
print(i1)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12, 13}

diff = setA.difference(setB)
print(diff)

#symmetric doesn't take the common elements 
diff1 = setA.symmetric_difference(setB)
print(diff1)

#setA.update(setB) # output {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
#setA.intersection_update(setB) # {1, 2, 3}
#setA.difference_update(setB) # {4, 5, 6, 7, 8, 9}
setA.symmetric_difference_update(setB) #{4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
print(setA)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 3}
set3 = {7, 8}
print(set1.issubset(set2)) #false
print(set2.issubset(set1)) #true
print(set1.issuperset(set2)) #True
print(set2.isdisjoint(set1)) #false bacause they have similar elements 
print(set2.isdisjoint(set3)) #true because they don't jave similar elements

#this doesn't copy, you assign to the same object
set4 = set2 
set4.add(7)
print(set2)
print(set4)

#to Copy 
set5 = set1.copy()
print(set5)
set6 = set(set2)
print(set6)


#Frozen set is also Collection data type and it is immutable
a = frozenset({1, 2, 3, 4})
#a.add(7) #error
#a.remove(1) #error because immutable 
print(a)







