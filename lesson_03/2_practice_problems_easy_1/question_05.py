# Starting with the string:

munsters_description = "The Munsters are creepy and spooky."

# print the string with the case of all letters swapped:
# "tHE mUNSTERS ARE CREEPY AND SPOOKY."

# My Solution

for i in munsters_description:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
print()

# Launch School Solution

print(munsters_description.swapcase())