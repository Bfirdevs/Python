#Errors and exceptions
#There are syntx errors and exceptions
#
a = 5 + '10' #unspoported operand type(s) for +: 'int' and 'str'
print(a)) # invalid syntax

import submodule  #module not found

d = 5 
b = c  # NameError / C is not defined 

f = open('somefile.txt') #FineNotFound 

e = [1,2,3]
e.remove(4) #valueError/ not in the list

my_dict = {'name' : 'Max'}
my_dict['age'] #Key error/ 
