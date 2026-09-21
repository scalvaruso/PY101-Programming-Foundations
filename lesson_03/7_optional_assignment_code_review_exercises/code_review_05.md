Your solution correctly identifies the elements at even indexes using `enumerate()` and `idx % 2 == 0`, which corresponds to the 1st, 3rd, 5th, etc. elements of the list. It also produces the expected results for the examples provided.

However, there is an important issue with using `None` as a marker for elements that should be discarded. `None` is a valid Python value and could itself be an element of the input list. For example:

```python
oddities([1, 2, None])
```

should return `[1, None]`, but your solution would remove the `None` and return `[1]`.

You can avoid this problem by adding the desired elements directly to the result list rather than first creating a list containing `None` values:

```python
def oddities(the_list):
    final_list = []

    for idx, val in enumerate(the_list):
        if idx % 2 == 0:
            final_list.append(val)

    return final_list
```

This also makes the solution simpler because you only need one loop instead of creating an intermediate list and then iterating over it again.

There is an even simpler way to express the operation using list slicing:

```python
def oddities(the_list):
    return the_list[::2]
```

The `::2` slice selects every second element starting with the first. This is concise and directly expresses what the function is supposed to do.

Your variable names are generally understandable. `idx` and `val` are reasonable names for an index and value, while `the_list` clearly communicates the type of the argument.

Overall, your approach demonstrates a good understanding of `enumerate()` and zero-based indexing, but the use of `None` as a placeholder introduces a correctness issue, and the two-stage construction makes the solution more complicated than necessary. Consider selecting the required elements directly, either with a loop or with list slicing.
