Your solution uses a reasonable approach, and the underlying leap-year logic is correct. In particular, the order of your conditions correctly handles century years such as 1900 and 2000.

There is, however, an indentation issue in the submitted code. The statements inside each `if` block should consistently use four spaces of indentation. In Python, indentation is part of the syntax, so inconsistent indentation can make the code difficult to read and may result in an `IndentationError` or `TabError`.

Your function and variable names are meaningful and follow Python's naming conventions. `is_leap_year` is especially clear because it describes a function that returns a Boolean value.

One area where the code could be simplified is the use of `is_a_leap_year`. You currently change its value in three separate `if` statements. Although this works, it requires the reader to keep track of how the value changes as each condition is evaluated.

You could make the control flow clearer by returning as soon as a condition determines the result:

```python
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True

    return False
```

This version closely follows the rules in the problem statement, avoids maintaining a separate variable, and makes the logic easier to follow.

Overall, you have a correct approach, but I would recommend fixing the inconsistent indentation and simplifying the control flow to make the solution clearer and easier to maintain.
