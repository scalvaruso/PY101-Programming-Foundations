# Write two different ways to remove all of the elements from the following list:

# My Solution

numbers = [1, 2, 3, 4]

numbers.clear()

print(numbers)

numbers = [1, 2, 3, 4]

del numbers[:]

print(numbers)

# Launch School Solution

# Approach 1
numbers = [1, 2, 3, 4]
numbers.clear()

# Approach 2
numbers = [1, 2, 3, 4]
while numbers:
   numbers.pop()

# NOTE that the following solution will set numbers to an empty list,
# but it doesn't clear the original list.
# That's fine if you know there are no other references to the list.

numbers = []
