""" PSEUDOCODE
START

# Given a collection of integers called "numbers"

SET iterator = 1
SET savedNumber = value within numbers collection at space 1

WHILE iterator <= length of numbers
    SET currentNumber = value within numbers collection at space "iterator"
    IF currentNumber > savedNumber
        savedNumber = currentNumber

    iterator = iterator + 1

PRINT savedNumber
"""

def find_greatest(numbers):
    iterator = 0
    saved_number = numbers[iterator]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number

        iterator += 1

    return saved_number

