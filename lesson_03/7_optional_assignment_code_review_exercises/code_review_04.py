# Iqbal's Solution

def compute(num, op):
  if op == '+':
    res = 0
    for i in range(1, num + 1):
      res += i
    return res
  elif op == '*':
    res = 1
    for i in range(1, num + 1):
      res *= i
    return res
  else:
    return None


  # These examples should all print True
print(compute(5, '+') == 15)
print(compute(6, '*') == 720)
print(compute(7, '-') == None)