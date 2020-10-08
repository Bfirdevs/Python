class Animal:
    #instantiate an object when it is created
    #this method will be called whenever we create the dog object
    # So we passed in a parameter and giving it a name 
    # dog = Animal("Tim")
    #The reasons for self that we need to invisibly pass the actual dog object parameter like Tim, Karabas
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

    def bark(self):
        print("bark")
    def meow(self):
        print("meow")
    def add_one(self, x):
        return x + 1

dog = Animal("Tim", 5)
dog.set_age(20)
print("Name is: " + dog.get_name())
print(dog.get_age())

dog1 = Animal("Karabas", 10)
print(dog1.get_name())
dog.bark()
print(dog.add_one(5))

