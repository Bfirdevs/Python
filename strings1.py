# Strings: ordered, immutable, text representation
# we can use both single or double quotes
# String formatting 

#this is all method
var = "Firdevs"
my_string = "the variable is %s " % var 
print(my_string)

var1 = 3
#d for decimal
#f for floating point
# %.2f means we want two digit after decimal
my_string1 = "the variable is %d " % var1
print(my_string1)

# This is the also old way
var2 = 3.243485
#to have decimal point {:.2f} 2 decimal point
my_string2 = "the varaible is {} and {} ".format(var2, var1)
print(my_string2)

#newest way

var3 = 3.45757895
var4 = 434
my_string4 = f"the variables are {var3*2} and {var2}"
print(my_string4)
