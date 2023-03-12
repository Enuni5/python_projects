### Working with Loops ###

# Do something repeatedly 

# While --> condition met = code execute

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # optional
    print("Condition is not met anymore")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("My condition is 15")
        break
    print("My condition is met")

print("Execution continues")

# For --> iterate over a list of elements

my_list = ['a', 'b', 'c', 'd', 'e']

for element in my_list:
    print(element)

# "element" is not a keyword, you can use whatever you want for that variable.
# It's valid for the other kind of groups of elements: tuples, sets and dicts (in this case shows the keys)

my_tuple = (1, 2, 3, 4)

for element in my_tuple:
    print(element)
else:
    print("Tuple is totally checked")

