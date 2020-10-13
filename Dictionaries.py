#Dictionaries are collection types that is unordered and mutable : Key-value pairs 
#Dictionaries are mutable, you can change the values after its creation
mydict = {"name": "Firdevs" , "age": 28, "city": "Texas"}
print(mydict)

mydict1 = dict(name="Mary", age=27, city="Boston")
print(mydict1)

value =  mydict["name"]
value1 = mydict["age"]
print(value)
print(value1)

mydict["email"] = "frdevs123@gmail.com"
print(mydict)
mydict["email"] = "firdevs@gmail.com"
print(mydict)