### Working with Exceptions ###

""" Sintaxis 
* try: --> Run this code 
* except: --> (may have a condition) execute this when an exception 
* else: --> No exceptions? Run this code 
* finally: --> Always run this code 
"""

number_one = 5
number_two = 1
number_two = "1" # if commented, there wont be errors

# try except

try:
    print(number_one + number_two)
    print("There are any errors")
except:
    print("There's an error")

# try except else
    
try:
    print(number_one + number_two)
    print("There are any errors")
except:
    print("There's an error")
else:
    # executed if no exceptions
    print("Execution continues correctly")

# try except else finally

try:
    print(number_one + number_two)
    print("There are any errors")
except:
    print("There's an error")
else:
    # executed if no exceptions
    print("Execution continues correctly")
finally:
    # always executed
    print("Execution continues")

# Catch exceptions by type

try:
    print(number_one + number_two)
    print("There are any errors")
except ValueError:
    print("There's a ValueError")
except TypeError: # There are other types of errors
    # Executed if TypeError exception
    print("There's a TypeError")

# Catch info of the exception

try:
    print(number_one + number_two)
    print("There are any errors")
except ValueError as error: # put the info of the error in the error variable (could be any variable name)
    print(error)
except Exception as exception:
    print(exception)