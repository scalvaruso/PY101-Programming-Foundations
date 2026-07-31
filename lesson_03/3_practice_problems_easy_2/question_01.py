# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# My Solution

reversed_numbers_1 = numbers[::-1]

reversed_numbers_2 = [number for number in reversed(numbers)]

print(reversed_numbers_1)
print(reversed_numbers_2)

# Launch School Solution

reversed_numbers = numbers[::-1]

reversed_numbers = list(reversed(numbers))
