Your solution has the right overall approach: you first determine the length of the string and then handle even- and odd-length strings separately. However, there is a functional issue in the even-length case.

You use `/` here:

```python
string[(l / 2) - 1] + string[l / 2]
```

In Python 3, `/` performs floating-point division. For example, `4 / 2` produces `2.0`, but string indexes must be integers. As a result, the even-length case raises a `TypeError`.

You should use floor division (`//`) instead:

```python
string[(l // 2) - 1] + string[l // 2]
```

There are also some indentation and formatting issues. Python's standard convention is to use four spaces for each indentation level. Your code currently mixes two- and four-space indentation. You should also include spaces around operators, so `l%2==0` becomes `l % 2 == 0`.

The variable name `l` is also not very descriptive and can easily be confused with `1` or `I`. A name such as `length` would make the code easier to understand. `middle_chars`, on the other hand, is a clear and meaningful name.

The if/else structure is appropriate for this problem, and there is no need for a loop or helper function.

A corrected version that keeps your original approach would be:

```python
def center_of(string):
    length = len(string)

    if length % 2 == 0:
        middle_chars = string[(length // 2) - 1] + string[length // 2]
        return middle_chars
    else:
        return string[length // 2]
```

You could also simplify the even-length case by using a slice,

```python
middle_chars = string[(length // 2) - 1:(length // 2) + 1]
```

but your original approach is perfectly reasonable once these issues are corrected.

Overall, the algorithm is on the right track, but the use of `/` instead of `//` means the submitted solution does not currently work for even-length strings. The inconsistent indentation, spacing, and ambiguous variable name should also be addressed to improve readability and consistency with Python conventions.