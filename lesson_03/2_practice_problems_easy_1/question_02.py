"""
How can you determine whether a given string ends with an exclamation mark (!)?
Write some code that prints True or False depending on whether the string ends with an exclamation mark.
"""

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False


# My Solution
def find_esclamation_mark(sentence):
    print(sentence[-1] == "!")


find_esclamation_mark(str1)
find_esclamation_mark(str2)

# Launch School Solution

print(str1.endswith("!"))  # True
print(str2.endswith("!"))  # False
