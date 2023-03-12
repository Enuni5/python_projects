### Working with Classes ###

class MyEmptyPerson:
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Any alias"): # This is the class constructor not a regular function
        self.full_name = f"{name} {surname} ({alias})"
        self.__name = name # This variable is now private with the __variable syntaxis
        self.__surname = surname # Also private var
    
    def get_name(self): # With this getter you can return the name from the class
        return self.__name

    def walk(self): # Needs the "self" parameter to access the other properties in the constructor
        print(f"{self.full_name} is walking")

my_person = Person("Emilio", "Núñez")
# print(f"{my_person.name} {my_person.surname}") # Now this is not working as those variables are private, they are not accessible
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Emilio", "Núñez", "Enuni")
print(my_other_person.full_name)

my_other_person.full_name = "Fulanito De tal (el Titán loco)" # But this is not changing the name, surname and alias variables in the constructor, it's changing the full_name variable
my_other_person.walk()
print(my_other_person.full_name)

print(my_other_person.get_name()) # The "name" value is now accesible from the get function.