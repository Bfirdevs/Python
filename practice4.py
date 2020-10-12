#Static in class methods 
#Class attributes
#self is referrring to instance of that specific context
# Class attributes are specific to class not an instance or object of the class

class Person: 
    number_of_people = 0


    def __init__(self, name):
        self.name = name
        Person.add_person()
    @classmethod 
    def num_of_people(cls):
        return cls.number_of_people
    
    @classmethod 
    def add_person(cls):
       cls.number_of_people += 1
    


p1 = Person("Firdevs")
p2 = Person("Elif")
print(Person.num_of_people())
