### Working with Functions ###

# Definition

def name_of_function ():
    print("This is a Function")

name_of_function ()

def sum(first_value, second_value):
    sum = first_value + second_value
    print(sum)

first_value = 1
second_value = 1

sum(first_value, second_value)

def function_that_returns (first, second):
    third = first + second
    return third

my_result = function_that_returns (first_value, second_value)

print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Núñez", name = "Emilio")

def print_name_with_default (name, surname, alias = "Any alias"): # Function with default value if not given
    print(f"{name} {surname} {alias}")

print_name_with_default("Emilio", "Núñez")
print_name_with_default("Emilio", "Núñez", "Enuni")

def print_texts(*text): # Any amount of parameters
    print(text)

print_texts("Hello", "Python", "Other")

def print_upper_texts (*texts):
    print(str(texts).upper())

print_upper_texts("this", "is", "a", "test")