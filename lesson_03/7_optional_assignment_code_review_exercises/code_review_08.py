"""
Write a function that takes a positive integer, n,
as an argument and prints a right triangle whose sides each have n stars.
The hypotenuse of the triangle (the diagonal side in the images below)
should have one end at the lower-left of the triangle,
and the other end at the upper-right.
"""

# Staff Solution and Explanation
"""
def triangle(height):
    for num in range(1, height + 1):
        spaces = height - num
        stars = num
        print(f'{" " * spaces}{"*" * stars}')
"""

"""
For this problem, we use a loop with the range function to iterate from 1 to height, inclusive. This helps us determine the number of stars to print in each line.

In each iteration of the loop:

    We determine the number of spaces to be printed as height - num. As num increases, the number of spaces decreases.
    We determine the number of stars to be printed as num. As num increases, the number of stars increases.

Python's string multiplication (*) is used to create a string with a repeated sequence of characters. This lets us generate the appropriate number of spaces and stars for each line of the triangle.
"""

# Kelly's Solution

def triangle(height):
    line = 1
    while line <= height:
        spaces = ''
        for _ in range(height - line):
            spaces += ' '

        stars = ''
        for _ in range(line):
            stars += '*'

        print(spaces + stars)
        line += 1


triangle(5)
"""
    *
   **
  ***
 ****
*****
"""

triangle(9)
"""
        *
       **
      ***
     ****
    *****
   ******
  *******
 ********
*********
"""