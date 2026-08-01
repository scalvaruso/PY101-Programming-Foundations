# Alan wrote the following function, which was intended to return all of the factors of number:

def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

"""
Alyssa noticed that this code would fail when the input is a negative number,
and asked Alan to change the loop.
How can he make this work?
Note that we're not looking to find the factors for negative numbers,
but we want to handle it gracefully instead of going into an infinite loop.
"""
# Bonus Question: What is the purpose of number % divisor == 0 in that code?

# My Solution

def factors(number):
    divisor = number
    result = []
    while divisor > 0:  # Replaced "!="
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

my_number = int(input())
print(factors(my_number))

# The purpose of number % divisor == 0 is to find the factors of number.
# number % divisor return the remainder of the division number / divisor
# A factor would divide exactly the number without returning any remainder
# Therefore would make the sentence True and add the divisor to the list of factors

# Launch School Solution

# Bonus Answer:
# It determines whether dividing the integer number
# by the integer divisor leaves a remainder of 0.
# That is, number % divisor == 0 is truthy if divisor is a factor of number.