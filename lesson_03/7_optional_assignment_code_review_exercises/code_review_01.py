"""
Print all odd numbers from 1 to 99, inclusive,
with each number on a separate line.
"""
# Ursula's Solution

i = 1
while i < 99:
    if i % 2 == 1:
        print(i)

    i = i + 1

"""
In your code review, you should be looking at the following:
  * Does the solution meet the problem requirements?
  * Is the code readable and easy to understand?
  * Do variable and function names adhere to Python naming conventions?
  * Are the variable and function names meaningful and precise?
  * Is the code formatted correctly and free of syntax errors?
  * Is the solution repetitive or overly complex?
  * Would it make more sense to use different looping or conditional structures?
  * Would the solution benefit from helper functions?
  * Consider running the code through PyLint and discussing any issues raised.
"""