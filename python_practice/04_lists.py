### Lists ###
# Lists are a collection of items in a particular order
# Lists are mutable, meaning the elements inside a list can be changed
# Lists are defined by having values between square brackets [ ]
# Lists can contain any type of variable, and they can contain as many variables as you wish
# Lists can also be sorted and sliced

new_list = ['a', 'b', 'c', 'd', 'e']
print(new_list)

# Accessing elements in a list
# Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired
# To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets
# Remember that Python considers the first item in a list to be at position 0, not position 1

print(new_list[0])

# Indexing a negative value will start counting from the end of the list

print(new_list[-1])

# Slicing a list

print(new_list[1:3])

# Looping through a list

for item in new_list:
    print(item)

# Checking if an item is in a list

if 'a' in new_list:
    print('Yes')   
else:
    print('No')

# List methods

# Adding items to a list

new_list.append('f')
print(new_list)

# Inserting items to a list

new_list.insert(0, 'z')
print(new_list)

# Removing items from a list

new_list.remove('z')
print(new_list)

# Removing items from a list by index

new_list.pop(0)
print(new_list)

# Sorting a list

new_list.sort()
print(new_list)

# Reversing a list

new_list.reverse()
print("List:" ,new_list)

# Copying a list

new_list_copy = new_list.copy()
print("List copy:", new_list_copy)

# Joining two lists

new_list_2 = ['g', 'h', 'i', 'j', 'k']  
new_list_3 = new_list + new_list_2
print("List 3:", new_list_3)

# List comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

new_list_4 = [x for x in new_list_3]
print("List 4:",new_list_4)

# List comprehension with conditionals

new_list_5 = [x for x in new_list_3 if x != 'g']
print("List 5:",new_list_5)

# List comprehension with conditionals and else

new_list_6 = [x if x != 'g' else 'z' for x in new_list_3]
print("List 6:",new_list_6)

# List comprehension with multiple for loops

new_list_7 = [x + y for x in new_list_3 for y in new_list_3]
print("List 7:",new_list_7)

# List comprehension with multiple for loops and conditionals

new_list_8 = [x + y for x in new_list_3 for y in new_list_3 if x != 'g']
print("List 8:",new_list_8)

# List comprehension with multiple for loops and conditionals and else

new_list_9 = [x + y if x != 'g' else 'z' for x in new_list_3 for y in new_list_3]
print("List 9:",new_list_9)

# List comprehension with multiple for loops and conditionals and else and functions

def add(x, y):
    return x + y

new_list_10 = [add(x, y) if x != 'f' else 'a' for x in new_list_3 for y in new_list_3]
print("List 10:",new_list_10)
