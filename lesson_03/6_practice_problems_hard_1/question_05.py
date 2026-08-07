# QUESTION

"""
What do you expect to happen when the greeting variable
is referenced in the last line of the code below?
"""

if False:
    greeting = "hello world"

print(greeting)

# My Solution

"""
I expect to receive a NameError.
the greeting variable is never initialized.
"""

# Launch School Solution

"""
In Python, referencing an uninitialized variable
will result in a NameError being raised.
This is because the if block is not executed
due to the False condition, and hence,
the greeting variable is never initialized.
"""