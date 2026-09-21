Your solution is readable and uses a straightforward approach. However, there is a small boundary issue: because your loop uses `while i < 99`, the value 99 is never processed, so the solution doesn't quite meet the requirement to include 99.

Changing the condition to `i <= 99` would fix this.

Your use of a while loop is valid, although a for loop with `range()` would be a natural choice here since we're iterating over a known range of numbers. You could also use the step argument to `range()` to generate only odd numbers and eliminate the conditional altogether.

The variable name `i` is acceptable for a loop counter, although something more descriptive such as `number` would make the code slightly easier to understand.