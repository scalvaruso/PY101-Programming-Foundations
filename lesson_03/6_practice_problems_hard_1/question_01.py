# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# My Solution

"""
No
The function first() will return the dic {'prop1': "hi there",}

The function second(), since the dic is on a line following return, will return None
"""

# Launch School Solution

"""
These functions do not return the same thing.
The function first() returns the expected value of { prop1: "hi there" },
but second() returns None without throwing any errors.
"""

"""
In Python, if there's nothing after a return statement,
the function will return None.
The indented block after the return statement in second
function is unreachable and doesn't affect the return value.
"""
