# dictionary: Key-Value pairs, unordered and mutable
my_dict = {'name': 'Firdevs', 
            'age': 28, 'city': 'Texas', 
            'email': 'frdevs123@gmail.com'}

my_dict1 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict1)
print(my_dict)

my_dict2 = {3: 9, 6: 36, 9: 81}
print(my_dict2)

value = my_dict2[3]
print(value)
mytuple = (8, 7)
#list are not hashable and cannot be used as a key
my_dict3 = {mytuple: 15}
print(my_dict3)