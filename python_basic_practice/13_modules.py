### Working with Modules ###

# It's like a library --> Code that is external to our present code file
# You are going to export/import

import my_module # import all the module

my_module.sumValues(1, 2) 
my_module.name_of_function()

# Import the "module" file and then you can access functions and other objects inside the module by the . notation

from my_module import name_of_function, sumValues # import only the objects you want and they are directly accesible
name_of_function()
sumValues(1, 4)

import math

print(math.sqrt(4))
print(math.pi)
print(math.factorial(10))
print(math.pow(2, 50))

from math import pi as PI_VALUE # import specific thing from module and give it an alias

print(PI_VALUE)