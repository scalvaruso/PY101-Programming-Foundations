"""
A double number is an even-length number whose left-side digits
are exactly the same as its right-side digits.
For example, 44, 3333, 103103, and 7676 are all double numbers,
whereas 444, 334433, and 107 are not.

Write a function that returns the number provided as an argument multiplied by two,
unless the argument is a double number.
If the argument is a double number, return the double number as-is.
"""


# Staff Solution and Explanation
"""
def is_double_number(number):
    string_number = str(number)
    center = len(string_number) // 2
    left_number = string_number[:center]
    right_number = string_number[center:]

    return left_number == right_number

def twice(number):
    if is_double_number(number):
        return number
    else:
        return number * 2
"""
"""
The logic for checking whether a number is a "double number" is maintained in the is_double_number function. Python's string slicing capabilities make it straightforward to compare the left half of the number to the right half.

    We convert the number into a string using the str function.
    Next, we find the midpoint (or center) of the string. We use integer division (//) to ensure we get an integer result.
    We then split the string into left_number and right_number using Python's slicing syntax.
    Finally, we check whether the left and right halves are equal and return the result.

The function twice checks whether the number is a "double number" and, depending on the result, returns the number itself or its doubled value.
"""

# Yosh's Solution

def twice(n):
  a = str(n)
  return n if len(a) % 2 == 0 and a[:len(a)//2] == a[len(a)//2:] else n*2


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True