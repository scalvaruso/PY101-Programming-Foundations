"""
In Python, every object has a unique identity that can be accessed using the id() function.
This function returns the identity of an object, which is guaranteed to be unique for the object's lifetime.
For certain basic immutable data types like short strings or integers,
Python might reuse the memory address for objects with the same value. This is known as "interning".
"""

# Given the following code, predict the output:

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))

# My Solution

# True

# Launch School Solution

# The output is True.
# Here, a and c reference the same object in memory, so their ids are the same.
# b will, in this case, have the same id as a and c due to interning.
# Therefore, the code will output True.

"""
In Python, there's a predefined range of integers, specifically from -5 to 256,
for which memory locations are pre-assigned.
When you reference an integer within this span,
Python consistently points to the same memory spot.
This strategy enhances efficiency since these particular numbers
are commonly utilized in many programming scenarios.

However, when you work with integers outside of this specific range,
Python doesn't assure that it will consistently point to the same memory address
for identical values across different variables.
"""
