Your solution correctly implements all three required cases. The addition and multiplication calculations are correct, and you correctly use `range(1, num + 1)` so that the supplied number is included. You also correctly return `None` when the operator is neither `'+'` nor `'*'`.

One thing to address is indentation. Your code consistently uses two spaces for each indentation level. While Python can execute code using a consistent indentation level other than four spaces, the standard Python convention is to use four spaces per indentation level.

For example:

```python
def compute(num, op):
    if op == '+':
        res = 0
        for i in range(1, num + 1):
            res += i
        return res
```

Consistent indentation is particularly important because indentation defines the structure of Python code. Mixing different indentation levels or tabs and spaces can result in `IndentationError` or `TabError`.

Your variable names are understandable, but `num`, `op`, and `res` are abbreviated. More descriptive names such as `number`, `operator`, and `result` could make the code easier to read.

There is also some repeated structure in your two branches. Both branches initialize a result, iterate through the same range, update the result, and return it. This is a good opportunity to consider whether the calculations could be separated into helper functions.

For example:

```python
def compute_sum(number):
    result = 0
    for current_number in range(1, number + 1):
        result += current_number
    return result


def compute_product(number):
    result = 1
    for current_number in range(1, number + 1):
        result *= current_number
    return result


def compute(number, operator):
    if operator == '+':
        return compute_sum(number)
    elif operator == '*':
        return compute_product(number)
    else:
        return None
```

This separates the two calculations from the decision about which calculation to perform. As a result, `compute()` has a very clear responsibility: it determines which operation the caller requested and delegates the actual calculation to the appropriate function.

The helper functions aren't strictly necessary for such a small problem, so the original approach is still reasonable. However, recognizing and appropriately separating repeated structure is a useful design consideration, particularly as programs become larger.

Overall, your solution has the correct logic and an appropriate basic structure. The main issue to fix is the indentation. More descriptive variable names and separating the repeated calculations into helper functions would further improve readability and organization.
