from functools import reduce 

#lambda
#this create a function with arguments and 
#it will evaulate the expression and return the results
#lambda arguments : expression
#we can write a function in one line 

#this takes and argument and add 10 and returns the result
add10 = lambda x: x+10
print(add10(5))

def add10_funct(x):
    return x + 10 


mult = lambda x, y: x * y
print(mult(2,7))

points2D = [(1,5), (15,1), (5,-1), (10,4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)
#function for lambda expression
def sort_by_y(x):
    return x[1]
 #We can say key = sort_by_y   
points_sorted = sorted(points2D, key = lambda x : x[1]) #index 1 is y so this will sort by y
print(points_sorted)

#sort by sum of x and 
points_sorted1 = sorted(points2D, key = lambda x : x[0] + x[1])
print(points_sorted1)

# map function
# map(func, seq)
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)
#this will do the same thing with lambda
c = [x*2 for x in a ]
print(c)
print(list(b))

#filter function 
#filter(func, seq)

d = filter(lambda x: x % 2 == 0 , a)
print(list(d))

d1 = [x for x in a if x % 2 == 0]
print(d1)

#reduce function
#reduce(func, seq)
product_a = reduce(lambda x, y : x * y , a) #multiplies all elemtents with each other
print(product_a) 








