### Practice with operators ###

#Arithmetics

print(39 + 3)
print(47 - 5)
print(6 * 7)
print(84 / 2)
print(42 % 2)
print(10 // 3) #Floor division --> Approximates division to integer (decimals leftover)
print(2 ** 3) #Exponent --> 2^3

# Trying tricks

print("Repeat this string " * 2)

new_float = 2 * 2.5
print("Repeat " * int(new_float))

# Compare things

print(4 > 2)
print(4 < 2)
print(4 >= 2)
print(4 <= 2)
print(4 & 2)
print(4 == 2)
print(4 != 2)

# Compare strings in an alphabetic order

print("hola" > "holi")
print("hola" < "holi")
print("hola" == "holi")
print("aaa" > "AAA") # lowercase > uppercase
print("bbb" < "AAA") 

# Logic operators

print(42 > 24 and 24 > 12)
print(42 < 24 or 24 > 12)
print(not (42 < 24) )
