Good work, Kelly! Your solution is correct and produces the required triangle for the given examples. Your use of a while loop, together with the separate construction of the spaces and stars, shows that you understand how the shape is built row by row.

A few improvements would make the solution simpler and more Pythonic:

Use string multiplication: Python allows strings to be repeated directly. Instead of building the spaces and stars one character at a time with two inner `for` loops, you can use:

```python
spaces = ' ' * (height - line)
stars = '*' * line
```

Consider a `for` loop: Since you know in advance that line needs to go from `1` through `height`, a `for` loop avoids manually initialising and incrementing the counter:

```python
for line in range(1, height + 1):
```

Reduce unnecessary repetition: Once string multiplication and a `for` loop are used, the entire solution can be expressed much more concisely.

For example:

```python
def triangle(height):
    for line in range(1, height + 1):
        print(' ' * (height - line) + '*' * line)
```

Your original solution is correct, so these are improvements in simplicity, readability, and Python idioms rather than fixes for a bug.

Keep up the good work! You're clearly understanding the underlying logic; the next step is becoming more familiar with Python's built-in features so you can express that logic more directly.
