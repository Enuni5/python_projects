### Working with strings ###

new_string = "This is a string declaration"  
other_string = 'Another way of declaring strings' 

print(len(new_string)) # Length of the string
print(other_string) # Print the string

string_with_quotes = "This string has \"quotes\" in it"
string_with_new_line = "This string has \n a new line in it"

print(string_with_quotes , string_with_new_line)

string_plus_tab = "This string has \t a tab in it"

print(string_plus_tab)

#Formatting strings

name, surname = "Emilio", "Núñez"

print("My name is {} {}".format(name, surname)) # Python 3.0
print("My name is %s %s" %(name, surname)) # Python 2.0
print("My name is %s %s" %("Emilio", "Núñez")) # Python 2.0
print(f"My name is {name} {surname}") # Python 3.6

#Accessing characters in a string with Indexing

language = "0123456789"
a, b, c, d, e, f, g, h, i, j = language # Unpacking
print(a, b, e, f, j) 

#Slicing strings

language_slice = language[1:4] # [start:stop]
print(language_slice)

language_slice = language[-3] # Negative indexing
print(language_slice)

language_slice = language[0:10:5] # [start:stop:step]
print(language_slice)

#Reverse a string

language_reverse = language[::-1] # [start:stop:step]
print(language_reverse) 

#String methods

language = "python"
print(language.upper()) # Uppercase
print(language.capitalize()) # Capitalize
print(language.title()) # Title
print(language.lower()) # Lowercase
print(language.swapcase()) # Swapcase
print(language.count("o")) # Count
print(language.find("o")) # Find
print(language.find("z")) # Find
print(language.replace("o", "a")) # Replace
print(language.split("o")) # Split
print(language.split("z")) # Split
print(language.isalpha()) # Check if all characters are letters
print(language.isdigit()) # Check if all characters are digits
print(language.isalnum()) # Check if all characters are alphanumeric
print(language.isspace()) # Check if all characters are whitespace
print(language.startswith("p")) # Check if string starts with
print(language.endswith("n")) # Check if string ends with
print(language.strip()) # Remove whitespace from start and end
print(language.lstrip()) # Remove whitespace from start
print(language.rstrip()) # Remove whitespace from end
print(language.center(20, "*")) # Center string