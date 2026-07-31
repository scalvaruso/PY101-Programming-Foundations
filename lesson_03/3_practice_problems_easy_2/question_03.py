# Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the same for the values 100 and 101.

# My Solution

print(10 <=  42 <= 100)
print(10 <= 100 <= 100)
print(10 <= 101 <= 100)

# Launch School Solution

42 in range(10, 101)          # True
100 in range(10, 101)         # True
101 in range(10, 101)         # False
