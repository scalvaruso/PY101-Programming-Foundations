# The following function unnecessarily uses two return statements
# to return boolean values.
# Can you rewrite this function so it only has one return statement
# and does not explicitly use either True or False?

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

# My Solution

def is_color_valid_revision_1(color):
    return color == "blue" or color == "green"

print(is_color_valid_revision_1("blue"))
print(is_color_valid_revision_1("green"))
print(is_color_valid_revision_1("red"))

def is_color_valid_revision_2(color):
    return True if color == "blue" or color == "green" else False

print(is_color_valid_revision_2("blue"))
print(is_color_valid_revision_2("green"))
print(is_color_valid_revision_2("red"))

# Launch School Solution

def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    return color in ["blue", "green"]
