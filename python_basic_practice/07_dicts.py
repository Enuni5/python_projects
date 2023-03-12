### Working with Dictionaries ###

new_dict = dict()
other_dict = {}

print(type(new_dict))
print(type(other_dict))

other_dict = {"Name" : "Emilio", "Surname" : "Núñez" , "Age" : 32, 1: "Python"}
print(other_dict)

new_dict = {
    "Name" : "Emilio", 
    "Surname" : "Núñez" , 
    "Age" : 32, 
    "Languages": {
        "Python",
        "Swift",
        "C"
        },
    1: 1.80
    }

print(len(new_dict))

print(new_dict["Languages"]) # You can access properties in the dict like that

# Update the value of a property

new_dict["Name"] = "Pepito"
print(new_dict["Name"])

# Add a property with its value

new_dict["City"] = "Torrox"
print(new_dict["City"])

# Removing propierties

del new_dict["City"]
# print(new_dict["City"]) --> KeyError: 'City'

# Find values in the dict

print("Emilio" in new_dict) # We are looking in the keys, not in the values so this will always be False.
print("Núñez" in new_dict)
print("Surname" in new_dict) # This is true as it is a property in the dictionary.

# Some methods

print(new_dict.items()) # Outputs every key/value pair in the dictionary
print(new_dict.keys()) # Outputs only the keys
print(new_dict.values()) # Outputs only the values

other_dict = dict.fromkeys(("Name", 1, "Country")) # Creates a new dictionary from the Keys passed as arguments and with empty values.
print(other_dict)

new_list = ["Alias", "Level", "Class", "Ability"]
another_dict = dict.fromkeys((new_list)) # You can also create the new dictionary and get the keys from a list
print(another_dict)

replicate_dict = dict.fromkeys(new_dict) # This is true power as you can replicate a dictionary with empty values and same keys
print(replicate_dict)
replicate_dict = dict.fromkeys(new_dict, ("Emilio", "Núñez")) # This adds the value desired (second argument) to every key
print(replicate_dict)

# It's possible to change its type too

new_values = replicate_dict.values()
print(type(new_values)) # This is now not a dict type is a dict_values type.

print(replicate_dict.values())
print(list(replicate_dict)) 
print(list(replicate_dict.values())) # Because it's now a dict_values, it can access dict values as list.
print(tuple(replicate_dict))
print(set(replicate_dict))