# itetools is a collection of tools for handling iterators 
#can be use in for loops
#offer advanced tools
#product
#permutation
#combinations
#accumulate
#groupby
# and infinite iterators 
from itertools import product 
from itertools import permutations
from itertools import combinations, combinations_with_replacement
from itertools import accumulate 
from itertools import groupby
import operator
from itertools import count, cycle, repeat 


a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(prod) # it says object we don't see element on the output = <itertools.product object at 0x000000A9FC24E680>
print(list(prod)) #output will display the elements [(1, 3), (1, 4), (2, 3), (2, 4)]

prod1 = product(a,b, repeat=2)
print(list(prod1))

#permutations
a = [1, 2, 3]
# we can also specify length permutations(a, 2)
perm = permutations(a)
print(list(perm))

#combinations 
a = [1, 2, 3, 4]
#we have to specify length in combination
comb = combinations(a, 2)
print(list(comb))
com_with_replacement = combinations_with_replacement(a, 2)
print(list(com_with_replacement))

#accumulators
a = [1, 2, 3, 4]
acc = accumulate(a)
acc1 = accumulate(a, func=operator.mul)

print(a) # [1, 2, 3, 4]
print(list(acc)) # [1, 3, 6, 10]
print(list(acc1)) # [1, 2, 6, 24]
b = [1, 2, 5, 3, 4]
acc2 = accumulate(b, func=max)
print(list(acc2)) #[1, 2, 5, 5, 5]

# Group By
def smaller_than_3(x):
    return x < 3
c = [1, 2, 3, 4]
group_obj = groupby(b, key = smaller_than_3)
#group_obj = groupby(b, key = lambda  x: x<3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))


persons = [{'name':'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
group_obj1 = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj1:
    print(key, list(value))

#Count
for i in count(10):
    print(i)
    if(i==15):
        break

a= [1, 2, 3]
for i in cycle(a):
    print(i)

for i in repeat(1, 4):
    print(i)
