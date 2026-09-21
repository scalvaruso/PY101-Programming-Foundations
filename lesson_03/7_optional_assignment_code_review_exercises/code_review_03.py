# Stephanie's Solution

def multisum(x):
    result = 0
    nums = list(range(1, x))
    for y in nums:
        if y % 3 == 0:
            result += y
        elif y % 5 == 0:
            result += y
    return result