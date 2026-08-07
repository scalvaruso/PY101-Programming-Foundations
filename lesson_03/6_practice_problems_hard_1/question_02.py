# What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# My Solution

# [1, 2]
# {'first': [1]}    # REVIEW

# Launch School Solution

# [1, 2]
# {'first': [1, 2]}

"""
Since num_list is a reference to the original list in dictionary,
appending to num_list modifies the list. Thus, the original dictionary is also updated.
If, instead of modifying the original dictionary,
we want to modify num_list but not dictionary, we have a couple of options:

    We can initialize num_list with a reference to a copy of the original list:
        dictionary = {"first": [1]}
        num_list = dictionary["first"].copy()
        num_list.append(2)

    We can use list slicing which returns a new list:
        dictionary = {"first": [1]}
        num_list = dictionary["first"][:]
        num_list.append(2)
"""