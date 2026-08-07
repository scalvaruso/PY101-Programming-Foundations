# QUESTION
# Given the following similar sets of code, what will each code snippet print?

#   ***   A   ***

def mess_with_vars(one, two, three):
    one = two 
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # ["one"]
print(f"two is: {two}")     # ["two"]
print(f"three is: {three}") # ["three"]

#   ***   B   ***

def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # ["one"]
print(f"two is: {two}")     # ["two"]
print(f"three is: {three}") # ["three"]

#   ***   C   ***

def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")     # ["two"]
print(f"two is: {two}")     # ["three"]
print(f"three is: {three}") # ["one"]

# My Solution

#   ***   A   ***

"""
Variable are assigned inside the function,
therefore they have a local scoop.
They are assigned the values existing in the global scoop,
but they are not returned, therefore the value printed
are those of the upper level variable, that have global scoop:

print(f"one is: {one}")     → ["one"]
print(f"two is: {two}")     → ["two"]
print(f"three is: {three}") → ["three"]

"""

#   ***   B   ***

"""
Variable are assigned inside the function,
therefore they have a local scoop.
Since they are not returned,
the value printed are those of the upper level variable
that have global scoop:

print(f"one is: {one}")     → ["one"]
print(f"two is: {two}")     → ["two"]
print(f"three is: {three}") → ["three"]

"""

#   ***   C   ***

"""
Variable are not assigned inside the function.
Function is changing the value at position [0] inside the variable.
Therefore the global variable will be modified and it will print:

print(f"one is: {one}")     → ["two"]
print(f"two is: {two}")     → ["three"]
print(f"three is: {three}") → ["one"]

"""

# Launch School Solution
