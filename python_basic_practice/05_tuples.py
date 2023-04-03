### Working with TUPLES ###

# A set of constant values

new_tuple = tuple()
another_tuple = ("hola", " ", "que", " ", "tal") 

new_tuple = (32, 1.80, "Emilio", "Núñez")
print(new_tuple)
print(type(new_tuple))

print(new_tuple[0])
print(new_tuple[-1])

print(new_tuple.count("Emilio")) # Counts the number of appearences of the value in the tuple
print(new_tuple.index(32)) # Return the index of the value in the tuple (if it exists)

# You can't re-assign values to elements in the tuple
# new_tuple[1] = 1.79 --> this throw an error
# print(new_tuple)

# But you can add elements to the tuple (via join)

joined_tuples = new_tuple + another_tuple
print(joined_tuples)

# You can find elements

print(joined_tuples[0:5:2])

# Change your tuple to a list

new_tuple = list(new_tuple)
print(type(new_tuple))

# Now change values

new_tuple[0] = 33
print(new_tuple)

# And go back to tuple if you need it

new_tuple = tuple(new_tuple)
print(type(new_tuple))
print(new_tuple)

# It's not supported item deletion from tuples

# del new_tuple[1] --> wont work

del new_tuple
# print(new_tuple) --> this would not work since new_tuple it's not defined.
