# What will the following two lines of code output?

print(0.3 + 0.6)
print(0.3 + 0.6 == 0.9)

# My Solution

# 0.9
# True

# Launch School Solution

"""
If you thought that the outputs would be 0.9 and True,
respectively, you were wrong.
Python uses floating point numbers for all numeric operations.
Most floating point representations used on computers lack a certain amount of precision,
and that can yield unexpected results like these.
"""
# In this case, the output was:

# 0.8999999999999999
# False

# The details of why this happens aren't crucial right now
# -- it's just something you need to be aware of.
# One way around the problem is to use the math.isclose function:

import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))

