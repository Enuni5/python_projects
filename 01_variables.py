# Variables in python practice

string_variable = "This is a string variable"

print(type(string_variable))

int_variable = 42

print(type(int_variable))

"""
I don't think I need to keep 
with this practice, it's very simple...
"""

# Best practices is using snake_case
# Best practices is using _ before keywords (like "if") --> _if

snake_case = "This is well named"
camelCase = "This is not well named"
_if_this_is_used = "This is also ok"

# More system functions

print(len(string_variable))

# Declare more than one variable at a time. DANGEROUS, not so a best practice.

name, surname, age, alias = "Emilio", "Núñez Nieto", 32, "Emi"

print("My name is",name, surname, "and I'm", str(age)+". People also call me", alias+".")

# Variables have flexible type, so be carefull

name = 32
age = "Emilio"

print("My name is",name, surname, "and I'm", age+". People also call me", alias+".")

# And you could do nothing about it

name: str = "Emilio"
age = 32

print("My name is",name, surname, "and I'm", str(age)+". People also call me", alias+".")

name = 32
age = "Emilio"

print("My name is",name, surname, "and I'm", age+". People also call me", alias+".")

# So be carefull when assinging values to variables, you might get lost for any reason.