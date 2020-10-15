# Strings: ordered, immutable, text representation
# we can use both single ot double quotes
my_string = "Hello World"
print(my_string)

a = 'I\'m a programmer'
print(a)
# """  triple quotes is used for documentation and multiline
# strings in our code
b  = """Hello 
World"""
print(b)

c = "HelloWorld"
char1 = c[0]
char2 = c[-1] #last
char3 = c[-2] #secondlast
print(char1)
print(char2)
print(char3)
substring = c[1:5]
print(substring)
substring1 = c[::2]
print(substring1)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)
for  i in sentence:
    print(i)

if "e" in sentence:
    print(True)
else:
    print(False)

names = "   aaaysee   "
names = names.strip()
print(names)
print(names.upper())
print(names.lower())
print(names.startswith('A'))
print(names.endswith('e'))
print(names.find('y')) # this will return index number 
print(names.count('a'))
print(names.replace('aaaysee', 'Firdevs Elif'))

my_string1 = 'how are you doing'
my_list = my_string1.split(" ")
print(my_list)

new_string = ' '.join(my_list)
print(new_string)

my_list1 = ['a'] * 6
print(my_list1)

#bad way
my_string2 = ''
for i in my_list1:
    my_string2 += i
print(my_string2)

#Goodway
my_string2 = ''.join(my_list1)
print(my_string2)


