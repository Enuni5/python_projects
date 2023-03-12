### Working with SETS ###

new_set = set()
other_set = {}

print(type(new_set))
print(type(other_set)) # Initialy type: dict.

other_set = {"Emilio", "Núñez", 35}
print(other_set)
print(type(other_set)) # Now it's a set. (As dictionaries have a defined structure of data inside the set).

print(len(other_set)) # Length is number of elements in the set.

# print(other_set[0]) --> This access pattern throw an error.

other_set.add("Una Cosa") # Sets are non-structured (not an order)
print(other_set)

other_set.add("Una Cosa") # You can't add duplicates (wont work).
print(other_set)

other_set.add("Otra Cosa") # You can't add duplicates (wont work).
print(other_set)

# Check if something is inside the set (as you can't access it by index).

print("Emilio" in other_set)
print("Emilia" in other_set)

other_set.clear() # Empty the set
print(other_set) 

# There are so many other methods with sets, just go check documentation when you need something done with them.

del other_set # This will delete this as with the other types.
# print(other_set) NameError: name 'other_set' is not defined

new_set = {"Emilio", "Núñez", 32}
new_list = list(new_set) # Change the type as you want with this function.
print(new_list) # This is risky as you don't know the orther of the set.
print(new_list[0]) # You are accessing an element but you don't know what it's as the set were not ordered.

other_set = {"una", "dos", 3, 42, 32, "Emilio"}
sets_united = other_set.union(new_set)
print(sets_united)

print(sets_united.difference(new_set))

another_set_method = other_set.intersection(new_set)
print(another_set_method)

