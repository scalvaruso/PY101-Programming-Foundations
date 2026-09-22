Good work, Leigh! Your solution has the correct overall structure and successfully handles valid and invalid responses. The `while True` loop is an appropriate choice here because the function needs to continue asking the question until the user provides a valid answer.

There are two important requirements that your solution is currently missing:

- **Handle uppercase and mixed-case input:** Your comparisons only recognise lowercase answers. For example, "Y", "YES", and "Yes" would be treated as invalid.
- **Strip leading and trailing whitespace:** Inputs such as " y " or "yes  " should be accepted, but your current code treats them as invalid.

You can address both requirements when reading the input:

```python
answer = input().lower().strip()
```

Your conditional logic is correct, but it could also be made slightly more Pythonic by using in rather than repeating the or comparison:

```python
if answer in ['y', 'yes']:
    ...
elif answer in ['n', 'no']:
    ...
```

The function and variable names are appropriate and follow Python's naming conventions. The formatting and indentation are also correct, and there are no syntax errors.

The return statements are a good choice here because they immediately exit the function once a valid answer has been received. No helper function is necessary for this exercise: the logic is simple enough to keep within `yes_no_response()`.

Overall, your solution has the right structure and is close to complete, but the case-insensitivity and whitespace requirements need to be addressed for the function to fully satisfy the specification.

Keep up the good work! You're using the loop and conditional structure effectively; now make sure to check all of the requirements, including the small input-handling details.
