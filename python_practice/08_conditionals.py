### Working with Conditionals ###

# Decide wether to run or not a snipet of code
# Make decisions in code

my_condition = False
my_second_condition = 4 * 2

if my_condition:
    print("The condition is executed")
elif my_second_condition >= 8:
    print("The second condition is executed")
else:
    print("The condition is NOT executed")


print("Execution continues")

""" Sytanxis: 
if - starts the check
and - add another condition to check
elif - another check in case first if doesn't check
else - in case anything is True, do this
You can use all logic operators in the if sentence
"""

my_string = ""

if my_string:
    print("This string is not empty")

if not my_string:
    print("This string is empty")