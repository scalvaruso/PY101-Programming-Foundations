print(True)  # True
print(False)  # False

def make_longer(string, longer):
    if longer:
        return string + string
    else:
        return string

print(make_longer("abc", True))  # 'abcabc'
print(make_longer("xyz", False))  # 'xyz'

def is_digit(char):
    if '0' <= char <= '9':
        return True
    else:
        return False

print(is_digit("5"))  # True
print(is_digit("a"))  # False

value = False  # or True

if value is True:
    print("It's true!")
elif value is False:
    print("It's false!")
else:
    print("It's not true or false!")


print(True or len(None))
print(False or "fallback")
print("" or "fallback")
print("" or False)
print(False or "")

print("***************")

print("hello" and "world")
print("" and "world")
print(0 and len(None))
print(5 and 10)

print("***************")

name = input("What is your name? ")

if name:
    print(f"Hi {name}")
else:
    print("you must enter your name!")