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

#deletes the name and its value
del mydict["name"]
print(mydict)
#deletes the age key value pair
mydict.pop("age")
print(mydict)
# removes the last element
mydict.popitem()
print(mydict)

if "name" in mydict1:
    print(mydict1["name"])

try:
    print(mydict1["age"])
except:
    print("Error")

for key in mydict1:
    print(key)

for key in mydict1.keys():
    print(key)

for value in mydict1.values():
    print(value)

for key, value in mydict1.items():
    print(key, value)


mydict2 = mydict1.copy()
mydict3 = dict(mydict1)
