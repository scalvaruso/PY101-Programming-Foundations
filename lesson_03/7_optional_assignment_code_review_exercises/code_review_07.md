Good work, Louisa! Your solution correctly implements the requirements and passes all of the provided examples, including the empty string and strings containing repeated digits.

Your use of a while loop and an index is valid, and you correctly account for the final character, where there is no following character to compare against.

A few areas could be improved:

- **Simplify the conditional logic:** Your nested if statements make the solution more complicated than necessary. Both branches ultimately add `text[i]`, so the conditions can be combined:

    ```python
    if i == len(text) - 1 or text[i] != text[i + 1]:
        result += text[i]
    ```

- **Use more descriptive names:** `i` is acceptable for an index, but `index` would make its purpose clearer. Similarly, `crunched_text` would be more descriptive than `result`.
- **Consider a for loop:** Since you are iterating through a string, a for loop can avoid manually managing the index and makes the code easier to follow.
- **Avoid unnecessary repetition:** `len(text)` is calculated several times. Storing it in `text_length` can improve readability and make the boundary conditions clearer.

Your solution is correct and demonstrates a good understanding of string indexing and conditional logic. The main opportunity now is to focus on simplifying the structure so that the code expresses the underlying idea as directly as possible.

Keep up the good work!