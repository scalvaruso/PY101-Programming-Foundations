# QUESTION

"""
Ben was tasked to write a simple Python function
to determine whether an input string is an IP address
using 4 dot-separated numbers, e.g., 10.4.5.11.

Alyssa supplied Ben with a function named is_an_ip_number.
It determines whether a string is a numeric string between 0 and 255
as required for IP numbers and asked Ben to use it.
"""

def is_an_ip_number(word):
    return int(word) in range(0,256)

"""
Here's the code that Ben wrote:
"""

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            break

    return True

'''
Alyssa reviewed Ben's code and said,
"It's a good start, but you missed a few things.
You're not returning a false condition,
and you're not handling the case when the input string
has more or less than 4 components,
e.g., 4.5.5 or 1.2.3.4.5: both those values should be invalid."

Help Ben fix his code.
'''

# My Solution

def is_dot_separated_ip_address_edit(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) == 4:
        for word in dot_separated_words:
            if not word.isdigit():
                return False
            if not is_an_ip_number(word):
                return False
        return True
    else:
        return False

ip_list = [
    "",
    "0",
    "A",
    "0.0",
    "0.0.0",
    "0.0.0.0",
    "255.255.255.255",
    "256.256.256.256",
    "257.257.257.257",
    "A.B.C.D",
    "0.0.0.0.0"
]

for ip in ip_list:
    try:
        result = is_dot_separated_ip_address(ip)
        print(f"Original function for ip '{ip}' returned '{result}'")
    except ValueError:
        print(f"'{ip}' is not valid for function 'is_dot_separated_ip_address'")

    try:
        result = is_dot_separated_ip_address_edit(ip)
        print(f"Modified function for ip '{ip}' returned '{result}'")
    except ValueError:
        print(f"'{ip}' is not valid for function 'is_dot_separated_ip_address_edit'")

# Launch School Solution

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while dot_separated_words:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True