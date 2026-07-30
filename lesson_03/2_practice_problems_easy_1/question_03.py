# Starting with the string:

famous_words = "seven years ago..."

"""
Show two different ways to create a new string with "Four score and "
prepended to the front of the string referenced by famous_words.
"""

# My Solution

print("Four score and " + famous_words)
print(f"Four score and {famous_words}")

# Launch School Solution
# String concatenation
new_string = "Four score and " + famous_words
# String interpolation
new_string = f"Four score and {famous_words}"